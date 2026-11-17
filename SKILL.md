---
name: designing-with-taste
description: Stops generic "AI slop" UI and pushes web, app and game interfaces toward distinctive, opinionated design grounded in the real subject. Use whenever building or restyling any page, landing page, menu, dashboard, component, slide or game UI, before choosing fonts, colours or layout. Also use when the user asks if something looks like AI slop, generic, template-y, boring or "AI made", wants a UI to look crazy, bold or unique, or wants an existing site audited for design quality.
---

# Designing with Taste

An LLM picks the most probable option. For an unconstrained design choice, the most probable option is the average of every tutorial it has seen, so with no constraint you produce the same page every time. That is slop: nothing in it was decided on purpose, so it could belong to any product. The cure is always the same shape: wherever you would reach for the default, make a specific decision that comes from this subject, and be able to say why.

Two modes:
- **Build mode**: making or restyling UI. Plan, check the plan, build, look at it, fix.
- **Review mode**: judging existing UI. Look at it for real, then give a verdict and fixes.

House rule: never use em dashes, in UI copy or in replies. Use a period, comma, colon or parentheses.

## The tells

**First-order slop** (the obvious house style)
- Purple, indigo or violet accent, decorative gradient, glowing blob behind the hero
- Inter, Geist, Poppins, Roboto or the system stack used flat for everything
- Identical rounded cards, one radius and one soft grey shadow on everything, cards inside cards
- Three icon cards in a row, emoji used as icons, sparkles, a pill badge above the headline
- Everything centered and evenly spaced, so nothing leads
- Hero, logos, 3 features, testimonials, pricing, CTA: the same skeleton regardless of subject
- Invented stats ("10x faster", "38% MoM"), quotes attributed to nobody, fake logo walls
- Fade-and-slide-up on every section, hover lift on every card, `transition: all`

**Second-order slop** (what "de-slopped" AI design now converges on, so it is a tell too)
- Warm cream paper (near #F4F1EA) + high-contrast serif (Fraunces, Playfair, Instrument Serif) + terracotta or clay accent (near #D97757)
- Near-black (#0B0B0B, #111) + one acid green or vermilion accent
- Broadsheet layout: hairline rules, zero radius, dense newspaper columns
- Template chrome: tracked-out ALL CAPS eyebrow above every heading, mono micro-labels on every number, "A · B · C" middot strings, a "→" on every button, 01 / 02 / 03 markers on content that is not a sequence, one word of the headline in a different colour or italic

Any of these can be right when the subject genuinely calls for it (a rickshaw meter really is an LED; a newspaper app really is a broadsheet). They become slop when they appear regardless of subject.

**Copy**
- Elevate, unlock, supercharge, seamless, empower, streamline, leverage, all-in-one, "build the future of"
- "It's not X, it's Y", forced triplets, em dashes
- Headlines that would fit any product

## The three dials

Bold is not always right. A crazy internal dashboard is as wrong as a beige landing page. Set three dials from 1 to 10 before planning, state them in one line, and let the user override them in chat ("boldness 3, motion 2, density 8"):

- **Boldness**: 1 is calm, symmetric and conventional; 10 is asymmetric, art-directed, rule-breaking.
- **Motion**: 1 is static; 10 is cinematic. Above 6 only when the subject is about energy or play.
- **Density**: 1 is an airy gallery; 10 is a cockpit full of data.

Starting points, adjusted to the subject: landing page or game menu 8 / 5 / 3, product app screen 4 / 3 / 6, internal dashboard or admin 2 / 2 / 8, docs or settings 2 / 1 / 5. Even at boldness 2 the page still needs a point of view; it just spends it in type, colour and copy instead of layout tricks.

## The core test

Cover the logo and the name. Could this page belong to any other product? Would you have produced nearly the same thing for a similar prompt? If yes to either, it is slop.

## Build mode

Copy this checklist and work through it:

```
- [ ] 1. Ground in the subject
- [ ] 2. Write the design plan
- [ ] 3. Check the plan against the defaults
- [ ] 4. Build
- [ ] 5. Render, look, and scan
- [ ] 6. Fix and remove one accessory
```

**1. Ground in the subject.** First look for a saved design system: a `DESIGN.md` in the project root, or existing CSS variables and theme files. If one exists, follow it and extend it instead of inventing a new look. Identify the product, its audience and the page's main job. If the brief does not say, propose them and confirm. Read the project and any memory for real material: the industry's objects, materials, vernacular, the words users actually say. Distinctive choices come from here. A Mumbai rickshaw game already has hazard tape, meter LEDs and "Horn OK Please" sitting there to use.

**2. Write the design plan** (short, before any code):
- **Point of view**: one line, named as a place, object or era from the subject's world, not an adjective. "Modern and clean" is not a point of view.
- **Colour**: 4 to 6 named hex values, with what each is for.
- **Type**: one or two families with clearly different jobs, and a real scale. Avoid families you would reach for on any project. See `references/choices.md`.
- **Layout**: a one-sentence concept plus a rough ASCII wireframe. Say the alignment (left, centered, justified) and what the first screen shows. Open with the most characteristic thing in the subject's world, not the default big-headline-plus-stats hero.
- **The one bold thing**: the single memorable element. Everything else stays quiet.

When the plan is agreed and the project has no `DESIGN.md`, save the plan there (point of view, dials, colours, type, layout rules, the one bold thing, banned defaults) so the next session keeps the same look instead of drifting back to defaults.

**3. Check the plan against the defaults.** Go through the tells above. For every part of the plan that matches one, or that you would also have produced for a similar prompt, revise it and tell the user in a line what you changed and why. If the user's brief explicitly asks for one of these looks, follow the brief: their words always win.

**4. Build.** If the project already uses a component library (shadcn/ui, Radix, MUI, its own components folder), install and restyle those components with the library's own tooling instead of hand-writing new ones; taste lives in the tokens and composition, not in reinvented dialogs. Rules that matter while coding:
- One dominant action per screen. If three buttons are equally loud, none wins.
- Vary radius, padding and weight so size and space show priority. Not everything is a card.
- Structure must carry information: numbering only for real sequences, labels only where they help, borders only where they group.
- Motion: one orchestrated moment beats scattered effects. Motion that answers a user action (open, confirm, expand) is welcome.
- Real content only. No invented stats, testimonials or user counts. If content is missing, use an obvious placeholder and say so.
- Design for hostile content: long names, empty, loading and error states, small screens.
- Quality floor, without announcing it: works at phone width with no sideways scroll, visible keyboard focus, `prefers-reduced-motion` respected, readable contrast, lines under about 80 characters.
- Copy: write from the user's side in plain words. Buttons say exactly what happens ("Save changes", not "Submit") and the same action keeps the same name through the flow. Errors say what went wrong and how to fix it. Sentence case. Local language (Hinglish etc.) is a strength when it fits the audience.

**5. Render, look, and scan.** Do not judge from code alone. A page that does not render is worth nothing, and a blank page "doesn't look AI" while being useless.
- Open it in a browser or headless browser, screenshot it at three sizes and look at every screenshot: desktop 1440x900, laptop 1366x768, phone 390x844. The laptop size matters because short screens are where content gets clipped: a tall block centred with `place-items: center` or `align-items: center` inside a scrolling container gets cut off at the top and cannot be scrolled back to (use `safe center` or top alignment). On each size check that nothing important is cut off at the top or bottom of the first screen. Check the console for errors.
- Click through the main flow (open, submit, error, empty state) and screenshot anything that changes. Fix overflow and overlapping elements you see at phone width.
- Run the scanner on the source: `python3 <this skill dir>/scripts/slop_scan.py <file or folder>`. It reports in `file:line` form:
  - **Slop tells**: overused fonts, purple hexes, gradients, uniform radius and shadows, `transition: all`, buzzwords, em dashes, arrows, middots, all-caps tracking. Each hit is a question, not an automatic failure: keep it only if you can say why this subject needs it.
  - **Access basics**: images without `alt`, icon-only buttons without `aria-label`, inputs without a label or `autocomplete`, `outline: none` with no `:focus-visible` replacement, animation with no `prefers-reduced-motion` handling. These are invisible in a screenshot but real for users, so fix them unless clearly a false positive.

**6. Fix and remove one accessory.** Fix what failed. Then, like checking the mirror before leaving the house, remove one piece of decoration that does not serve the subject.

**Making several screens or slides?** They should share one system but not collapse into sameness. If you are making several separate artifacts for different briefs, make them diverge on ground colour, display type family and accent, so they do not look like one designer's template.

## Review mode

Look, do not guess:
1. Screenshot it at 1440x900, 1366x768 and 390x844 and view the images. Look for clipped content on the short laptop screen as well as style.
2. Read the main stylesheet: fonts, colour variables, gradients, radius and shadow values.
3. Run `scripts/slop_scan.py` on the source if you have it.
4. Read the visible copy.

Report in this shape:

**Verdict**: Slop / Partly generic / Not slop, in one line, with the main reason.

**What works** (keep these): specific choices that give it a point of view, with evidence (font names, real copy lines, colours).

**What still looks generic**: numbered, most important first. Each says what you saw and why it reads as a default.

**Access and polish issues**: terse `file:line` list from the scanner and the screenshots (missing labels, focus, reduced motion, overflow). Skip the section if there are none.

**How to push it further**: 3 to 5 concrete ideas that grow out of the existing point of view, not a new unrelated style.

Be honest in both directions. If it is good, say so plainly and do not invent problems. If it is slop, say it kindly but clearly. Broken details (missing glyphs, tofu boxes, overflowing text, console errors) count as heavily as style, because they make anything feel cheap.

## Prompting another AI for UI

When the user wants a prompt for another tool, name the point of view, the exact fonts and hexes, the layout idea, the real content, and a "do not use" list built from the tells above. Example:

> Point of view: a Mumbai local train ticket. Colours: ticket pink #F2B8C6, ink #20202A, stamp red #C8102E. Type: Big Shoulders Display for headings, Mukta for body. Left-aligned, the main form shaped like the ticket with a perforated edge. Copy is about [the real product], casual, some Hinglish. Do not use: gradients, identical rounded cards, emoji icons, a 3-feature grid, invented stats, all-caps eyebrow labels, arrows on buttons.
