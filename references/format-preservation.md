# Format Preservation Contract

Use this reference before creating or editing final soft-copyright deliverables.

## Formatting Source Priority

Use formatting sources in this order:

1. A user-provided completed package for the same or latest project.
2. A local completed-format directory such as `assets/completed-format-example/`.
3. A local completed-format archive such as `assets/completed-format-example.zip`.
4. `assets/official-software-copyright-templates.zip`.

Never overwrite these sources. Copy or extract them into the current application workspace first.

## Required Final File Set

A normal single-software package should end with these files in `提交材料/` or the final package root:

- `软件著作权登记审批表-2026.xlsx`
- `2-GPL声明.docx`
- `源程序.docx`
- `软件使用手册or设计说明书.docx`
- `代码.zip`

Do not submit Markdown replacements for these Office files.

## Safe Editing Rules

- For `.xlsx`, use an existing workbook and update cell values only. Preserve merged cells, dimensions, borders, alignment, fonts, sheets, and print settings.
- For `.docx`, use a copied template/example document. Replace placeholders or paragraph/table contents while keeping styles, section properties, headers, footers, page numbers, and image anchors.
- Prefer a directory-format completed example over a zip when copying files, because it avoids ZIP filename-encoding ambiguity.
- Do not rebuild final Office files from Markdown unless the user explicitly accepts possible manual reformatting.
- Do not flatten images into low-resolution screenshots of pages.
- Do not remove the cover page, table of contents, source-code headers, or official declaration layout.

## Manual / Design Specification Figures

The manual/specification cannot be all text. It should contain actual inserted figures or screenshots.

For structure diagrams, workflow diagrams, and polished result figures, use a locally available Nature-style figure skill when possible.

Follow that figure skill's backend gate. If it requires a Python/R selection and the user has not selected one, ask `Python or R?` and wait. Once selected, use only that backend for figure rendering, preview, and export.

Recommended minimum figure set:

- `图 1 系统总体结构图`
- `图 2 运行流程图`
- `图 3 终端运行输出`
- result figure/table preview when applicable

## Terminal Screenshot Rule

The run-effect screenshot should be easy for the user to reproduce and visually clean:

- avoid Chinese paths in the visible command;
- avoid shell scripts as the visible command unless the software itself is a shell tool;
- avoid noisy environment setup output;
- use concise English output if the screenshot is illustrative;
- keep generated helper scripts in an ASCII path such as the project root;
- never expose credentials, patient/sample private data, internal server addresses, or raw omics paths.

It is acceptable to create a virtual/demo screenshot helper when the user wants a clean screenshot, as long as the manual text does not falsely claim it processed confidential production data.

## QA Checklist

Before final delivery:

- unzip the final package listing and confirm the exact required file names exist;
- open or inspect the Office containers enough to confirm they are real `.docx`/`.xlsx`, not renamed text files;
- check names, versions, dates, legal entity, programming language, and source line count are consistent;
- check the manual has inserted image relationships in `word/_rels/document.xml.rels`;
- check `代码.zip` does not contain `__MACOSX`, `.DS_Store`, `.git`, caches, virtual environments, raw data, or large generated outputs.
