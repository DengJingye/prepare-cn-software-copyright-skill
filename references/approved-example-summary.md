# Approved Example Summary

This reference summarizes the structure of a previously approved package. It is intentionally anonymized for public use. Use it as a style and completeness reference, not as text to copy blindly.

## File Set

- `软件著作权登记审批表-2026.xlsx`
- `2-GPL声明.docx`
- `源程序.docx`
- `软件使用手册or设计说明书.docx`
- `代码.zip`

## Registration Form Pattern

The example includes:

- 软件全称: a concise bioinformatics analysis software name
- 软件简称: a short abbreviation distinct from the full name
- 版本号: `V1.0`
- 软件分类: `应用软件`
- 软件作品说明: original software
- 开发方式: cooperation development
- 发表状态: unpublished
- 编程语言: the actual project language, such as `Python`, `R`, `Bash Shell`, or mixed languages
- 源程序量: counted source lines
- 面向领域: `生命科学`

The long main-function text uses a useful four-module pattern:

1. 原始数据解析与特征过滤
2. 样本质控与全局对齐基准计算
3. 基于流式引擎的细胞级比例抽样
4. 表达矩阵构建与全流程验证

Use an analogous module pattern for future omics software:

1. input parsing and validation;
2. preprocessing/normalization/QC;
3. core algorithm/model/pipeline;
4. output/report/export/downstream compatibility.

## Design Specification Pattern

The approved design specification uses:

1. 引言
   - 项目背景和核心问题
   - 开发目标与核心价值
   - 设计哲学与技术特点
2. 系统架构与流程
   - layered architecture
   - core components
   - business/data flow
3. 核心模块详细设计
4. 环境准备与安装
5. 输入与输出文件详解
6. 快速使用指南
7. 常见问题与 Troubleshooting

This pattern works especially well for command-line omics pipelines and research software.

## Source Package Pattern

The source zip contains a top-level `代码/` folder with authored shell scripts, including controller scripts and step scripts. Avoid keeping `__MACOSX` or `.DS_Store` in future archives even if the approved historical example had platform-generated artifacts.

## GPL Statement Pattern

The approved example follows:

```text
GPL声明
我单位独立开发的软件“[软件全称]”[版本号]，没有使用和修改Linux核心源代码，仅使用了[语言/运行环境]运行环境，并未使用和修改任何遵循GPL协议的自由软件源代码，因此本软件不遵循GPL协议。
特此声明。
[法人单位]
[日期]
```

Keep the legal entity and date aligned with the application package.
