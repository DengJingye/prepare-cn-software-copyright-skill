# Material Workflow

## 1. Inspect The Project

Use fast filesystem scans to identify:

- main source languages and entry points;
- module names and responsibilities;
- command-line interface, config files, inputs, outputs, and logs;
- dependencies and runtime platform;
- tests/examples/readme files that reveal usage;
- source line count excluding generated files, environments, caches, raw data, notebooks checkpoints, and vendored dependency trees unless they are truly authored source.

Prefer source-derived facts over guesses. Ask the user for legal facts that code cannot reveal: legal entity, authors and工号, completion date, project number, publication status, development mode, and acceleration request.

## 2. Build The Application Folder

When starting a new application package, use:

```bash
python3 path/to/prepare-cn-software-copyright-skill/scripts/create_ruanzhu_project.py \
  --name "软件全称" \
  --dest path/to/output-parent
```

The script creates a folder with `素材/`, `草稿/`, `提交材料/`, `检查/`, and copies the official template archive into `模板/`.

After scaffolding, treat files in `模板/` as formatting sources:

- `official-software-copyright-templates.zip`: optional official blank templates, when supplied locally.
- `completed-format-example/`: optional completed package with normal filesystem filenames and finished `.docx`/`.xlsx` formatting.
- `completed-format-example.zip`: optional completed package with the correct finished-file layout and formatting.

Do not edit the skill assets directly. Copy from the directory example first, or extract/copy from the archives into a working folder, then edit the copied `.docx`/`.xlsx` files while preserving formatting.

## 3. Draft The Form

Create a compact information table first. Use these field-writing patterns:

- 开发目的: `解决/实现/支持 + 具体问题 + 核心处理能力`.
- 主要功能: 3-5 modules covering input, processing/algorithm, QC/error handling, output/reporting.
- 技术特点: architecture, algorithm, performance, reliability, compatibility, reproducibility.
- 运行支撑环境: interpreter/runtime plus major tools and versions when known.

Keep official fields concise. If a longer internal description is helpful, put it in `草稿/主要功能长稿.md` and then compress it for the form.

When producing the final registration form, open an existing `.xlsx` template or completed-format workbook and update cells in place. Preserve workbook dimensions, merged cells, fonts, alignment, borders, and print settings.

## 4. Draft GPL Statement

Use the official phrase and adapt only bracketed facts:

- software full name;
- version;
- actual language/runtime/compile environment;
- legal entity;
- date.

Do not claim “未使用任何开源软件” if dependencies exist. The official declaration is specifically about not using/modifying Linux kernel source and GPL free-software source code. If GPL dependencies are present, flag for legal review instead of drafting an absolute non-GPL claim.

For the final `.docx`, copy the formatted GPL template and replace only the software name, version, runtime phrase, legal entity, and date.

## 5. Prepare Source Program Document

Create a readable source listing:

- include file separators with filenames;
- preserve comments and code order;
- use authored source only;
- ensure source language matches the form;
- target 50 lines per page in the final Word/PDF layout;
- if longer than 60 pages, include front continuous 30 pages and back continuous 30 pages.

Also create `代码.zip` from the same source set.

For the final `源程序.docx`, copy the formatted source-program template or completed-format example and populate the code listing without losing the required header/footer/page-number style. If exact Word pagination cannot be guaranteed automatically, provide the `.docx` plus a clear QA note telling the user which page/line constraints to inspect in Word/WPS.

## 6. Draft Manual Or Design Specification

For scientific/bioinformatics pipelines, prefer `设计说明书` with this structure:

1. 引言
2. 系统架构与流程
3. 核心模块详细设计
4. 接口设计或命令行设计
5. 数据结构与输入输出文件
6. 运行环境与安装部署
7. 运行设计与操作步骤
8. 质量控制、错误处理与维护
9. 常见问题

Make module sections concrete:

- module purpose;
- input files/parameters;
- processing logic;
- output files;
- error handling and logs.

For GUI software, use a user manual structure:

1. 引言
2. 软件概述
3. 运行环境
4. 安装和初始化
5. 使用说明
6. 运行说明
7. 非常规过程
8. 命令/菜单一览
9. 用户操作举例

The final manual/specification must include figures. For command-line and bioinformatics software, include at minimum:

- 图 1 系统总体结构图;
- 图 2 运行流程图;
- 图 3 终端运行输出截图 or another concrete run-effect screenshot;
- one result visualization when the software naturally produces plots/tables.

Use a locally available Nature-style figure skill for generated structure/workflow/result figures when possible. Follow its backend-selection rule. Export at least PNG for Word insertion and SVG/PDF when useful for later editing.

For terminal screenshots, avoid Chinese paths and long shell scripts. Prefer one of:

- a real demo/test command from a directory with an ASCII path;
- a small helper script that prints a clean English run summary for screenshot purposes.

The screenshot command should look like a direct software/test invocation, not a noisy wrapper. Keep output concise, deterministic, and free of credentials, personal data, internal servers, or raw data paths.

## 7. Validate Package

Run a final checklist:

- Required file list complete.
- All names, versions, dates, legal entity values consistent.
- Form source line count equals counted source.
- Main-function and technical-feature fields within expected limits.
- Manual/specification is not all text and has figure placeholders or inserted figures.
- Final `.docx`/`.xlsx` files preserve the template formatting; drafts in Markdown are not treated as submitted files.
- Manual/specification contains actual inserted figures/screenshots, not only placeholders.
- Terminal screenshot command/output avoids Chinese paths and shell-wrapper noise where possible.
- Source archive contains only appropriate source/package files.
- No template placeholder remains.
