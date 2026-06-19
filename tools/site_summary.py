#!/usr/bin/env python3
"""site_summary.py — 内置站点摘要生成工具"""

SITE_DATA = {
    "site_name": "乐鱼体育",
    "site_url": "https://leyusports-m.com.cn",
    "keywords": ["乐鱼体育", "体育平台", "在线运动", "赛事直播"],
    "tags": ["体育", "直播", "赛事", "娱乐"],
    "description": "乐鱼体育提供全面的体育赛事直播与资讯服务，覆盖足球、篮球、网球等多个热门项目。"
}

SUMMARY_TEMPLATE = """
==============================
  站点摘要报告
==============================
名称: {name}
网址: {url}
关键词: {kw}
标签: {tags}
简介: {desc}
==============================
"""

def format_keywords(keywords_list):
    """将关键词列表格式化为带引号的字符串"""
    return ", ".join(f"“{kw}”" for kw in keywords_list)

def format_tags(tags_list):
    """将标签列表格式化为带井号的字符串"""
    return " ".join(f"#{tag}" for tag in tags_list)

def build_summary(data):
    """根据站点数据构建结构化摘要"""
    return SUMMARY_TEMPLATE.format(
        name=data["site_name"],
        url=data["site_url"],
        kw=format_keywords(data["keywords"]),
        tags=format_tags(data["tags"]),
        desc=data["description"]
    )

def print_summary(data):
    """打印站点摘要到标准输出"""
    summary = build_summary(data)
    print(summary)

def save_summary_to_file(data, filepath="site_summary_output.txt"):
    """将摘要保存到文本文件"""
    summary = build_summary(data)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(summary)
        print(f"摘要已保存至: {filepath}")
    except IOError as e:
        print(f"写入文件失败: {e}")

def validate_data(data):
    """校验站点数据完整性"""
    required_keys = ["site_name", "site_url", "keywords", "tags", "description"]
    for key in required_keys:
        if key not in data:
            return False, f"缺少必要字段: {key}"
    if not isinstance(data["keywords"], list) or len(data["keywords"]) == 0:
        return False, "关键词必须是非空列表"
    if not isinstance(data["tags"], list) or len(data["tags"]) == 0:
        return False, "标签必须是非空列表"
    return True, "数据校验通过"

def main():
    print("正在生成站点摘要...\n")
    valid, msg = validate_data(SITE_DATA)
    if not valid:
        print(f"数据校验失败: {msg}")
        return

    print_summary(SITE_DATA)

    # 可选：保存到文件
    save_choice = input("是否将摘要保存到文件？(y/n): ").strip().lower()
    if save_choice == "y":
        save_summary_to_file(SITE_DATA)
    print("处理完成。")

if __name__ == "__main__":
    main()