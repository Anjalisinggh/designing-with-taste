# designing-with-taste

Take the blind taste test: https://site-one-umber-77.vercel.app/

An agent skill that stops generic "AI slop" UI and pushes pages, apps, dashboards and game menus toward design with a real point of view.

## What it does

- **Build mode**: sets three dials (boldness, motion, density), grounds the design in the real subject, writes a short plan, checks it against known AI defaults, builds, screenshots at 1440x900, 1366x768 and 390x844, runs a scanner, then fixes what fails. Saves the plan to `DESIGN.md` so later sessions keep the same look.
- **Review mode**: screenshots a live site, reads its CSS and copy, runs the scanner and gives a verdict (Slop / Partly generic / Not slop) with evidence and fixes that grow out of the existing style.

It knows both kinds of slop:
- **First order**: purple gradients, Inter, identical rounded cards, three-icon feature grids, buzzword copy.
- **Second order**: what "tasteful" AI design converges on now, such as cream + high-contrast serif + terracotta, near-black + acid accent, ALL CAPS eyebrows, mono micro-labels, arrows on every button.

## Install

Clone it into your agent's skills folder:

```bash
git clone https://github.com/Anjalisinggh/designing-with-taste.git <skills-folder>/designing-with-taste
```

Your agent picks it up automatically. Ask for any UI, or ask "is this AI slop?", or force it with `/designing-with-taste`.

## Scanner

```bash
python3 scripts/slop_scan.py path/to/file-or-folder
```

Reports overused fonts, purple hexes, gradients, uniform radius and shadows, buzzwords, em dashes, arrows, middots, all-caps labels, plus access basics (missing alt, unlabeled buttons, missing autocomplete, removed focus outlines, animation without reduced-motion). Every slop hit is a question, not an automatic failure. Python 3 standard library only.

## Layout

```
SKILL.md                 main instructions
references/choices.md    type, colour and layout menu (loaded only when needed)
scripts/slop_scan.py     mechanical checks
evals/                   test cases (prompt + graders per case)
site/                    landing page (Astro), deployed to GitHub Pages by .github/workflows/deploy-site.yml
```

## Test results (iteration 1)

Three prompts (chai stall landing page, gym front-desk dashboard, review of a live game menu), each run with and without the skill:

| | With skill | Without |
|---|---|---|
| Checks passed | 93% | 79% |

Without the skill, both build tasks drifted into second-order slop (cream, serif or terracotta, ALL CAPS labels) and one invented business facts. With it, the chai page became a painted tin signboard and the dashboard used gym weight-plate colours for status.

## Landing page

The site lives in `site/` and is built with Astro.

```bash
cd site
npm install
npm run dev
```

Every push to `main` that touches `site/` rebuilds it and publishes it to GitHub Pages.
