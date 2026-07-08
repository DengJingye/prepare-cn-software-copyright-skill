# prepare-cn-software-copyright-skill

一个用于辅助撰写和整理中国软件著作权申请材料的 Codex skill，适合命令行工具、生信分析软件、科研脚本、数据处理管线、后端服务等项目。

它可以帮助 Codex 按软著材料习惯检查项目、整理信息、生成草稿、创建材料工作区，并提醒保留 Word/Excel 模板格式，避免把 `.docx` / `.xlsx` 材料变成纯文本或低保真文档。

## 能做什么

- 梳理软著申请所需信息：软件全称、简称、版本号、开发环境、运行环境、源程序量、主要功能、技术特点等。
- 整理一个干净代码仓库：保留 README、测试数据/示例、预期输出或结果展示，剔除旧备份、缓存、大型结果、真实数据和内部路径。
- 创建软著材料工作区：`模板/`、`素材/`、`草稿/`、`提交材料/`、`检查/`。
- 指导准备常见提交材料：
  - 软件著作权登记审批表或信息收集表
  - GPL 声明
  - 源程序文档
  - 代码压缩包
  - 软件使用手册或设计说明书
  - 必要时的合作开发合同
- 强调格式保真：最终 `.docx` / `.xlsx` 应从模板复制后修改，保留页眉、页脚、表格、目录、图片、页码等格式。
- 提醒手册/设计说明书必须包含系统结构图、仓库结构与模块职责图、运行流程图、终端运行输出示意图和必要结果/QC图，不能只有纯文字。
- 默认版本号使用 `V1.0`；源程序文档不加数字行号，并去除不必要空白代码行。
- 最终交付面向用户时只保留干净代码仓库和最终提交材料压缩包，不把中间文档或辅助材料作为最终成果。

## 安装

把这个仓库克隆到 Codex 的 skills 目录：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/DengJingye/prepare-cn-software-copyright-skill.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/prepare-cn-software-copyright"
```

如果你已经克隆过，后续更新：

```bash
cd "${CODEX_HOME:-$HOME/.codex}/skills/prepare-cn-software-copyright"
git pull
```

## 快速开始

在 Codex 里对你的项目说：

```text
Use $prepare-cn-software-copyright to prepare Chinese software copyright materials for this project:
/path/to/your/software-project

软件全称：XXX软件
版本号：V1.0
申请单位：XXX单位
```

也可以先只创建材料工作区：

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/prepare-cn-software-copyright/scripts/create_ruanzhu_project.py" \
  --name "XXX软件" \
  --dest /path/to/output-parent
```

生成的目录结构类似：

```text
XXX软件/
├── 模板/
├── 素材/
│   └── 待收集信息.md
├── 草稿/
├── 提交材料/
└── 检查/
    └── 软著材料检查清单.md
```

## 推荐工作流

1. 让 Codex 读取项目代码，识别入口脚本、主要模块、输入输出、依赖和源程序量。
2. 补充代码无法判断的法律/项目信息，例如申请单位、开发人员、完成日期、开发方式、发表状态。
3. 使用脚本创建软著材料工作区。
4. 把官方模板或你自己的已完成格式母版放入 `模板/` 或 skill 的 `assets/` 本地目录。
5. 先生成 Markdown 草稿，再复制到 Word/Excel 模板中，或者在可保留格式的工具链里直接修改 `.docx` / `.xlsx`。
6. 为手册或设计说明书准备图片：系统总体结构图、软件仓库结构与模块职责图、软件运行流程图、终端运行输出示意图、结果图或表格预览。图注/图题放在图片上方。
7. 生成源程序文档时去掉不必要空白行，不添加数字行号；代码压缩包来自干净代码仓库/源码集。
8. 最后按 `检查/软著材料检查清单.md` 检查文件名、版本号、页眉页脚、图片、源程序量和压缩包内容。

## 可选模板资产

公开仓库不包含真实软著材料、官方 Office 模板、完成版 `.docx` / `.xlsx`、PDF、截图或代码压缩包。

私有使用时，可以在本地添加：

```text
assets/
├── official-software-copyright-templates.zip
├── completed-format-example/
└── completed-format-example.zip
```

这些文件会被脚手架复制到新项目的 `模板/` 目录中。请不要把真实申请材料提交到公开仓库。

## 手册图片与运行截图建议

软著手册或设计说明书通常不能只有纯文字。建议至少准备：

- 图 1 系统总体结构图
- 图 2 软件仓库结构与模块职责图
- 图 3 软件运行流程图
- 图 4 终端运行输出示意图
- 结果图、QC图或结果表预览

如果你本地有 Nature-style figure / scientific figure 相关 skill，可以让 Codex 用它生成结构图、流程图和结果图。软件仓库结构与模块职责图也可以先输出 Markdown 树状图，用户自行截图。终端截图建议使用不含中文路径、不暴露敏感信息的 demo 命令或测试命令。

示例提示：

```text
请用 $prepare-cn-software-copyright 为这个 Python 命令行软件准备软著材料。
手册中需要包含系统结构图、运行流程图、终端运行截图和结果图。
终端截图请使用不含中文路径的演示命令。
```

## 安全注意事项

不要公开提交以下内容：

- 真实 `.docx` / `.xlsx` 申请材料
- 代码压缩包、内部项目代码、未公开数据
- 单位联系人、手机号、邮箱、身份证件、合同
- 医疗、患者、样本、内部服务器或数据库路径
- GitHub token、API key、密码、证书

本仓库的 `.gitignore` 默认会排除常见 Office、PDF、图片和压缩包材料，但上传前仍建议运行：

```bash
git status
git ls-files
```

确认没有真实申请材料被跟踪。

## 仓库结构

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── ASSETS.md
├── references/
│   ├── approved-example-summary.md
│   ├── format-preservation.md
│   ├── material-workflow.md
│   └── official-requirements.md
└── scripts/
    └── create_ruanzhu_project.py
```

## License / 免责声明

本项目提供的是材料整理和写作辅助流程，不构成法律意见。正式提交前，请按当地/单位最新要求和实际模板进行人工复核。
