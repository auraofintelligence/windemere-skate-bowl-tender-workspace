# Windemere skate bowl tender workspace

This is an exploratory tender collaboration workspace for Redland City Council Tender PDG-20842-1, Skate Bowl Refurbishment, Windemere Road Park, Alexandra Hills.

It is not official Redland City Council material. It is not VFG's final tender submission. It is not engineering advice. It is not for construction.

The workspace helps organise tender facts, role boundaries, questions, tasks, draft CAD workflow and tender response thinking for a possible Strange But True x VFG collaboration.

## Public/private caution

The GitHub Pages site may be public, so keep the raw tender PDFs, Word files, spreadsheets, prices, signatures, private contact details, filled returnables and commercial-in-confidence material out of this repository.

The `.gitignore` file blocks common tender document formats and private folders. Keep source documents locally outside the repo unless the team has agreed they can be published.

## Licence

All rights reserved. See `LICENSE.md`.

## Suggested workflow

1. Add uploaded tender docs locally outside this repo.
2. Review the website pages before the site visit.
3. Capture site notes and update `data/questions.json` and `data/tasks.json`.
4. Confirm role split and role boundaries.
5. Decide bid / no-bid.
6. Draft returnables and concept CAD.
7. VFG and relevant specialists review before anything goes to Council.

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
