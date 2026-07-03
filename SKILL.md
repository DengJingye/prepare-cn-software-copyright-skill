---
name: prepare-cn-software-copyright
description: Prepare Chinese software copyright application materials for biological, bioinformatics, pipeline, analysis, command-line, or research software. Use when drafting, checking, or organizing 中国软件著作权/软著申请 deliverables, including 软件著作权登记审批表/信息收集表, GPL声明, 源程序文档, 源代码压缩包, 软件使用手册或设计说明书, and cooperation-development contract materials.
---

# Prepare Chinese Software Copyright

## Overview

Use this skill to turn a software project into a complete Chinese software copyright application package. Preserve consistency across all documents: software full name, short name, version, applicant/legal entity, development mode, completion date, programming language, source line count, and technical description.

## First Pass

1. Inspect the target project or existing application folder.
2. Read `references/official-requirements.md` before drafting or checking official-format materials.
3. Read `references/format-preservation.md` before creating or editing `.docx` or `.xlsx` deliverables. This is mandatory.
4. Read `references/material-workflow.md` when creating a new package from scratch.
5. Read `references/approved-example-summary.md` when matching the style of the approved real example.
6. Use `scripts/create_ruanzhu_project.py` to scaffold a new material folder when the user asks to start a new application package.

## Non-Negotiable Format Rule

The final deliverables must keep the official/approved file formats. Do not replace `.docx` or `.xlsx` files with Markdown, plain text, HTML, or newly generated low-fidelity documents. Start from a copied official template or the completed-format example, then edit content inside the existing Office container while preserving:

- page size, margins, headers, footers, page numbers, table layout, fonts, styles, and section breaks;
- cover page and table-of-contents structure in the manual/specification;
- source-program page header requirements and line/page layout;
- embedded figures, captions, and screenshot placement.

If a tool cannot preserve formatting, stop and say so; produce Markdown only as draft text for manual insertion, not as a submitted file.

## Deliverables

Prepare or check these files unless the user narrows the scope:

- `软件著作权登记审批表` or `软件著作权信息收集表`: structured metadata and short official descriptions.
- `GPL声明.docx` or draft text: legal-entity declaration; use法人单位落款.
- `源程序.docx`: front 30 pages and back 30 pages of source, or all source if under 60 pages; every page should contain at least 50 source lines except unavoidable ending page constraints.
- `代码.zip`: source-code archive for upload/checking; exclude generated caches and platform junk such as `__MACOSX`, `.DS_Store`, `.git`, large outputs, raw data, and virtual environments.
- `软件使用手册or设计说明书.docx`: choose design specification for backend, pipeline, CLI, algorithm, or research software; choose user manual for GUI/product workflow software. This file must contain clear figures/screenshots, not text alone.
- `项目合作开发合同`: only when multiple legal entities jointly apply.

## Information To Collect

Collect these before drafting, inferring from code where possible and asking only for missing legal/project facts:

- 软件全称, 软件简称, 版本号.
- 申请/著作权法人单位, 联系人, 部门, 项目名称及编号.
- 开发人员/作者姓名和工号.
- 软件分类, 软件作品说明, 开发方式, 开发完成日期, 发表状态.
- 开发硬件环境, 运行硬件环境, 开发操作系统, 开发工具, 运行平台, 支撑环境.
- 编程语言 and total source line count.
- 开发目的 within about 50 Chinese characters, 面向领域/行业 within about 50 Chinese characters.
- 主要功能 and 技术特点 with the official field length limits in mind.

## Writing Style

- Use formal, objective Chinese: “本软件用于…”, “系统支持…”, “模块实现…”.
- Emphasize concrete software behavior, not research background alone.
- For bioinformatics software, describe input data, preprocessing, algorithm/core method, QC/checks, output files, downstream compatibility, and reproducibility.
- Keep all document names and version strings byte-for-byte consistent.
- Avoid claiming novelty beyond the code; describe technical features as implementation characteristics.
- Do not include secrets, raw omics data, credentials, patient data, internal server paths, or private database contents.

## Document Strategy

- Prefer `设计说明书` for scripts, pipelines, command-line tools, algorithms, and backend services. Include architecture, modules, processing flow, data structures, interface/command design, error handling, and running environment.
- Prefer `使用手册` only when there are user-facing screens or a clear operation workflow. Include screenshots when available.
- For design specifications, generate or insert actual diagrams whenever possible. If a Nature-style figure skill is available locally, use it for system architecture diagrams, workflow diagrams, result visualizations, and other polished manual figures. Follow that figure skill's backend gate exactly.
- Include a terminal running screenshot. Prefer a clean ASCII-only command/output from a helper script or test/demo run placed in a non-Chinese path, so the screenshot does not expose Chinese paths or noisy shell wrappers.
- Use the approved example's structure for scientific pipelines: 引言, 系统架构与流程, 核心模块详细设计, 环境准备与安装, 输入与输出文件, 快速使用指南, 常见问题.

## Assets

- Optional local official template archive: `assets/official-software-copyright-templates.zip`.
- Optional local completed-format example directory: `assets/completed-format-example/`.
- Optional local completed-format example archive: `assets/completed-format-example.zip`.

This public skill does not bundle real completed application materials. If local formatting assets are present, use the completed-format example directory first when preserving finished `.docx`/`.xlsx` formatting. Use archives as backup/reference material. Do not overwrite template or completed-format assets.
