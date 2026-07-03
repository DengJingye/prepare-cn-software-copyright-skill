#!/usr/bin/env python3
import argparse
import shutil
from pathlib import Path


def safe_folder_name(name: str) -> str:
    return "".join(ch for ch in name.strip() if ch not in "\\/:*?\"<>|").strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Chinese software copyright application workspace.")
    parser.add_argument("--name", required=True, help="软件全称, used as the folder name")
    parser.add_argument("--dest", default=".", help="Parent directory for the new application folder")
    parser.add_argument("--template-zip", default=None, help="Optional official template zip to copy")
    args = parser.parse_args()

    folder_name = safe_folder_name(args.name)
    if not folder_name:
        raise SystemExit("Empty or invalid software name")

    root = Path(args.dest).expanduser().resolve() / folder_name
    root.mkdir(parents=True, exist_ok=True)

    for sub in ["模板", "素材", "草稿", "提交材料", "检查"]:
        (root / sub).mkdir(exist_ok=True)

    checklist = root / "检查" / "软著材料检查清单.md"
    if not checklist.exists():
        checklist.write_text(
            f"""# {args.name} 软著材料检查清单

- [ ] 软件全称、简称、版本号在所有文件中完全一致
- [ ] 最终 .docx/.xlsx 文件基于模板/完成版复制编辑，未丢失页眉页脚、表格、目录、图片等格式
- [ ] 登记审批表/信息收集表填写完整
- [ ] GPL声明已按法人单位落款
- [ ] 源程序文档已按前30页+后30页或不足60页全量整理
- [ ] 源程序每页不少于50行，页眉含软件名/版本/页码
- [ ] 代码.zip 已生成且不含 .git、__MACOSX、.DS_Store、缓存、环境、原始数据
- [ ] 使用手册或设计说明书正文不少于15页
- [ ] 文档已插入结构图、流程图、终端运行截图和必要结果图，不是纯文字
- [ ] 手册图片使用 nature-figure skill 或等质量方式生成，清晰可读
- [ ] 终端截图命令/输出不含中文路径、敏感信息或嘈杂 shell 包装
- [ ] 项目合作开发合同是否需要已确认
- [ ] 无 [XXXX]、_____ 等模板占位符
""",
            encoding="utf-8",
        )

    notes = root / "素材" / "待收集信息.md"
    if not notes.exists():
        notes.write_text(
            f"""# {args.name} 待收集信息

- 软件全称：
- 软件简称：
- 版本号：
- 著作权法人单位：
- 联系人及联系方式：
- 项目名称及编号：
- 开发人员（姓名+工号）：
- 软件分类：
- 软件作品说明：
- 开发方式：
- 开发完成日期：
- 发表状态：
- 开发硬件环境：
- 运行硬件环境：
- 开发操作系统：
- 开发工具：
- 运行平台/操作系统：
- 运行支撑环境/支持软件：
- 编程语言：
- 源程序量：
- 开发目的：
- 面向领域/行业：
- 主要功能：
- 技术特点：
""",
            encoding="utf-8",
        )

    skill_dir = Path(__file__).resolve().parents[1]
    default_template = skill_dir / "assets" / "official-software-copyright-templates.zip"
    template = Path(args.template_zip).expanduser().resolve() if args.template_zip else default_template
    if template.exists():
        shutil.copy2(template, root / "模板" / template.name)

    completed_format = skill_dir / "assets" / "completed-format-example.zip"
    if completed_format.exists():
        shutil.copy2(completed_format, root / "模板" / completed_format.name)

    completed_format_dir = skill_dir / "assets" / "completed-format-example"
    target_format_dir = root / "模板" / "completed-format-example"
    if completed_format_dir.exists() and not target_format_dir.exists():
        shutil.copytree(completed_format_dir, target_format_dir)

    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
