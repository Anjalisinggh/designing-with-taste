#!/usr/bin/env python3
"""Count mechanical AI-slop tells in UI source files.

Usage: python3 slop_scan.py <file-or-folder> [more paths...]

Scans .html .css .scss .js .jsx .ts .tsx .vue .svelte .astro .md files.
Each hit is a question to answer ("does this subject need it?"), not an automatic failure.
Exit code is always 0; this is a report, not a gate.
"""
import os
import re
import sys
from collections import Counter

EXTS = {".html", ".css", ".scss", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".astro", ".md", ".mdx"}
SKIP_DIRS = {"node_modules", ".git", ".next", "dist", "build", "out", ".svelte-kit", "coverage", "vendor"}
# Minified bundles are noise: compiled framework code, not design decisions.
MAX_LINE_LEN = 2000

CHECKS = [
    ("overused font (first order)", r"\b(Inter|Geist|Poppins|Roboto|Open Sans|Montserrat)\b"),
    ("overused font (second order)", r"\b(Space Grotesk|DM Sans|Plus Jakarta Sans|Manrope|Outfit|Fraunces|Playfair Display|Instrument Serif|DM Serif Display|Rozha One|Abril Fatface)\b"),
    ("system font stack as main face", r"font-family:\s*(system-ui|-apple-system|ui-sans-serif)"),
    ("purple/indigo hex", r"#(6366f1|8b5cf6|818cf8|7c3aed|a855f7|4f46e5|9333ea|a78bfa|c084fc)\b"),
    ("purple/indigo Tailwind class", r"\b(from|to|via|bg|text)-(purple|indigo|violet)-\d{3}\b"),
    ("cream + terracotta kit", r"#(f4f1ea|f5f0e8|faf7f2|d97757|c96442|cc785c)\b"),
    ("gradient", r"(linear|radial|conic)-gradient\(|\bbg-gradient-to-"),
    ("blur / glass effect", r"backdrop-filter|backdrop-blur|blur-3xl"),
    ("transition: all", r"transition:\s*all|\btransition-all\b"),
    ("buzzword copy", r"\b(elevate|unlock|supercharge|seamless(ly)?|empower|streamline|leverage|all-in-one|revolutioni[sz]e|game-?changer|next-level)\b"),
    ("'not X, it's Y' flip", r"\bnot (just |only )?\w+[,.]? (it'?s|but)\b"),
    ("em dash", "\u2014"),
    ("arrow glyph on text", "→|&rarr;"),
    ("middot separator", "·|&middot;"),
    ("sparkle / emoji icon", "✨|\U0001F680|\U0001F525|⚡"),
]

RADIUS_RE = re.compile(r"border-radius:\s*([^;}\"']+)|\brounded(-[a-z0-9]+)?\b")
SHADOW_RE = re.compile(r"box-shadow:\s*([^;}\"']+)|(?<![-\w])shadow-(sm|md|lg|xl|2xl)\b")
CAPS_TRACK_RE = re.compile(r"text-transform:\s*uppercase|\buppercase\b.*\btracking-")

# Access basics. Regex over markup is approximate: expect some false positives and say so.
MARKUP_EXTS = {".html", ".jsx", ".tsx", ".vue", ".svelte", ".astro"}
IMG_RE = re.compile(r"<img\b[^>]*>", re.I | re.S)
BUTTON_RE = re.compile(r"<button\b([^>]*)>(.*?)</button>", re.I | re.S)
INPUT_RE = re.compile(r"<input\b[^>]*>", re.I | re.S)
NON_TEXT_INPUT = re.compile(r"type\s*=\s*[\"'{]*(hidden|submit|button|checkbox|radio|range|color|file|reset|image)", re.I)
LABEL_ATTR = re.compile(r"aria-label|aria-labelledby|\btitle\s*=", re.I)


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def access_checks(path, text, out):
    for m in IMG_RE.finditer(text):
        if not re.search(r"\balt\s*=", m.group(0), re.I):
            out["image without alt"].append(f"{path}:{line_of(text, m.start())}")
    for m in BUTTON_RE.finditer(text):
        attrs, inner = m.group(1), m.group(2)
        visible = re.sub(r"<[^>]+>", "", inner).strip()
        if not visible and not LABEL_ATTR.search(attrs):
            # Empty markup with no icon inside usually means JS fills the label later: verify in the rendered page.
            key = ("icon-only button without aria-label" if re.search(r"<(svg|img|i|span)\b", inner, re.I)
                   else "empty button (label probably set by JS; verify in the rendered page)")
            out[key].append(f"{path}:{line_of(text, m.start())}")
    for m in INPUT_RE.finditer(text):
        tag = m.group(0)
        if NON_TEXT_INPUT.search(tag):
            continue
        if not re.search(r"autocomplete|autoComplete", tag):
            out["text input without autocomplete"].append(f"{path}:{line_of(text, m.start())}")
        if not re.search(r"\bid\s*=|aria-label", tag, re.I):
            out["input with no id or aria-label (label cannot point at it)"].append(f"{path}:{line_of(text, m.start())}")


def iter_files(paths):
    for p in paths:
        if os.path.isfile(p):
            yield p
        elif os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
                for f in files:
                    if os.path.splitext(f)[1].lower() in EXTS:
                        yield os.path.join(root, f)
        else:
            print(f"skip: {p} not found", file=sys.stderr)


def main(argv):
    if not argv:
        print(__doc__)
        return 0
    hits = {name: [] for name, _ in CHECKS}
    compiled = [(name, re.compile(rx, re.IGNORECASE)) for name, rx in CHECKS]
    radii, shadows = Counter(), Counter()
    caps = 0
    nfiles = 0
    access = {k: [] for k in ("image without alt", "icon-only button without aria-label",
                              "empty button (label probably set by JS; verify in the rendered page)",
                              "text input without autocomplete",
                              "input with no id or aria-label (label cannot point at it)")}
    outline_none, focus_visible, motion, reduced = [], False, [], False
    for path in iter_files(argv):
        nfiles += 1
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                lines = fh.readlines()
        except OSError as e:
            print(f"skip: {path}: {e}", file=sys.stderr)
            continue
        text = "".join(lines)
        if os.path.splitext(path)[1].lower() in MARKUP_EXTS:
            access_checks(path, text, access)
        for m in re.finditer(r"outline:\s*(none|0)\b|\boutline-none\b", text):
            outline_none.append(f"{path}:{line_of(text, m.start())}")
        focus_visible = focus_visible or bool(re.search(r"focus-visible", text))
        for m in re.finditer(r"@keyframes|animation:|\banimate-\w+", text):
            motion.append(f"{path}:{line_of(text, m.start())}")
        reduced = reduced or bool(re.search(r"prefers-reduced-motion|motion-reduce|useReducedMotion", text))
        for i, line in enumerate(lines, 1):
            if len(line) > MAX_LINE_LEN:
                continue
            for name, rx in compiled:
                m = rx.search(line)
                if m:
                    hits[name].append(f"{path}:{i}: {m.group(0)!s}")
            for m in RADIUS_RE.finditer(line):
                radii[(m.group(1) or m.group(0)).strip()] += 1
            for m in SHADOW_RE.finditer(line):
                shadows[(m.group(1) or m.group(0)).strip()] += 1
            if CAPS_TRACK_RE.search(line):
                caps += 1

    print(f"Scanned {nfiles} file(s).\n")
    found = False
    for name, _ in CHECKS:
        h = hits[name]
        if h:
            found = True
            print(f"[{len(h)}] {name}")
            for x in h[:5]:
                print(f"      {x}")
            if len(h) > 5:
                print(f"      ... {len(h) - 5} more")
    if not found:
        print("No pattern hits.")

    print("\nStructure signals:")
    total_r = sum(radii.values())
    if total_r:
        top, n = radii.most_common(1)[0]
        share = n / total_r
        flag = "  <- one radius everywhere? add hierarchy" if total_r >= 5 and share > 0.6 else ""
        print(f"  border-radius: {total_r} uses, {len(radii)} distinct, most common '{top}' = {share:.0%}{flag}")
    total_s = sum(shadows.values())
    if total_s:
        top, n = shadows.most_common(1)[0]
        flag = "  <- same shadow on everything?" if total_s >= 4 and n / total_s > 0.6 else ""
        print(f"  box-shadow: {total_s} uses, most common '{top[:50]}' x{n}{flag}")
    if caps:
        flag = "  <- all-caps labels everywhere?" if caps >= 6 else ""
        print(f"  uppercase text: {caps} lines{flag}")
    print("\nAccess basics (regex, approximate; check each):")
    items = list(access.items())
    if outline_none and not focus_visible:
        items.append(("outline removed and no :focus-visible anywhere", outline_none))
    if motion and not reduced:
        items.append(("animation with no prefers-reduced-motion handling", motion))
    shown = False
    for name, h in items:
        if h:
            shown = True
            print(f"  [{len(h)}] {name}")
            for x in h[:5]:
                print(f"        {x}")
            if len(h) > 5:
                print(f"        ... {len(h) - 5} more")
    if not shown:
        print("  No hits.")
    print("\nEach slop hit is a question: keep it only if this subject needs it.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
