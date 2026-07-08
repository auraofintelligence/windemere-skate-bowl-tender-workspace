# Windemere skate bowl tender workspace

This is an exploratory tender collaboration workspace for Redland City Council Tender PDG-20842-1, Skate Bowl Refurbishment, Windemere Road Park, Alexandra Hills.

It is not official Redland City Council material. It is not VFG's final tender submission. It is not engineering advice. It is not for construction.

The workspace helps organise tender facts, role boundaries, questions, tasks, draft CAD workflow and tender response thinking for a possible Strange But True x VFG collaboration.

## Public/private caution

The blank/source tender pack is included in `tender-documents/` for easy public review by project direction.

Keep filled returnables, prices, signatures, private contact details, supplier quotes, private evidence and commercial-in-confidence material out of this repository.

The `.gitignore` file blocks private working folders while allowing the published source tender pack.

## Licence

All rights reserved. See `LICENSE.md`.

## Suggested workflow

1. Review the website pages and `tender-documents/` source pack before the site visit.
2. Capture site notes and update `data/questions.json` and `data/tasks.json`.
3. Confirm role split and role boundaries.
4. Decide bid / no-bid.
5. Draft returnables and concept CAD in a private working area.
6. VFG and relevant specialists review before anything goes to Council.

## Local preview

From this folder, run:

```powershell
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/
```

The site is plain HTML, CSS and JavaScript. There is no frontend build step.

## GitHub Pages

The site is designed to publish from the repository root on the `main` branch.
