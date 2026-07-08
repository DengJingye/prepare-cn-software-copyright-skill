# Official Requirements Summary

Source: official template package and `0-请先阅读本文件！.txt`.

## Required Materials

- `软件著作权登记审批表` / `软件著作权信息收集表`.
- `GPL声明`: not always mandatory, but often prepared; the落款 must be the legal法人单位.
- `源程序代码` document.
- `软件使用手册` or `设计说明书`.
- `项目合作开发合同`: only when multiple legal persons jointly apply or cooperation-development proof is required.
- Source-code/software zip package for upload and verification.

## Naming And Version Rules

- 软件全称 must be short, clear, targeted, and consistent across every file.
- Recommended naming pattern: `品牌 + 产品用途与功能 + 软件/系统/平台/插件/中间件`.
- Names ending in `工具`, `计算`, `系列` should be used cautiously.
- 软件简称 is an abbreviation of the full name; it must not be identical to the full name. Leave blank if there is no short name.
- Version should use `V1.0` by default for new packages unless the user explicitly provides another version.
- The presence/case of `V` must stay identical in all materials.

## Registration Form Fields

- 主要功能 and 技术特点 must be accurate and detailed within the official limit. Current reviewer feedback may require the 主要功能 field to be 500-1300 Chinese characters; obey that range when requested by policy/reviewer or when the current template has room for it. If a specific official form enforces a shorter byte/character limit, compress only after preserving a complete draft.
- 开发目的: about 50 Chinese characters.
- 面向领域/行业: about 50 Chinese characters.
- Hardware/software environment fields: about 50 characters each.
- 编程语言 must include every language represented in the source-code document.
- 源程序量 must match the submitted source-code document and source archive.

## Source Program

- General deposit: submit the first continuous 30 pages and last continuous 30 pages of source code.
- If the source program is under 60 pages, submit all source code.
- Each page should contain at least 50 lines of code.
- The final page should be an ending page of a program.
- Page header: left software name, center version, right page number.
- Also upload the source-code zip archive for checking.
- Do not add numeric line numbers to the source listing unless the template explicitly requires them.
- Remove unnecessary blank source lines from the submitted listing while preserving code order and meaning.

## Manual Or Design Specification

- Page 1 must be cover.
- Page 2 must be table of contents with accurate page numbers.
- Except cover, each page header should show: left software name, center version, right page number. The table-of-contents page is page 1.
- Except cover, each page should contain at least 30 lines of text unless that page contains a figure.
- Body content excluding cover and table of contents should be at least 15 pages.
- The document cannot be all text.
- User manuals should include relevant UI screenshots, login interface if applicable, operation screenshots, and text explanation.
- Design specifications should include software structure diagrams, functional flowcharts, logic diagrams, overall design, interface design, module/function descriptions, algorithms, data structures/data dictionary, and running design.
- Screenshots/figures must be clear.
- Figure captions/titles should appear above figures when producing new manuals/specifications, unless the user's fixed template requires another position.

## GPL Declaration

Template wording:

```text
GPL声明
我单位独立开发的软件“[软件名称]”[版本号]，没有使用和修改Linux核心源代码，仅使用了[编译/运行环境]，并未使用和修改任何遵循GPL协议的自由软件源代码，因此本软件不遵循GPL协议。
特此声明。
[法人单位名称]
[日期]
```

Adjust the environment phrase to the actual software stack, such as `Python 运行环境`, `R 运行环境`, `Bash 运行环境`, or a compiled-language environment.

## Cooperation Contract

- Required for multiple legal entities applying jointly or when cooperation-development proof is needed.
- Not required for a single legal-entity independent application.

## Final Check

Before delivery, check every file for:

- identical software full name and version;
- consistent applicant/legal entity;
- line count matching between form, source document, and code archive;
- no template placeholders such as `[XXXX]` or `_____`;
- no private credentials, internal paths that should not be disclosed, raw data, or large generated outputs;
- no `.DS_Store`, `__MACOSX`, `.git`, cache folders, virtual environments, or binary/raw data in `代码.zip`.
