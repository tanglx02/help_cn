import argparse
import sys
import os
import json
from pathlib import Path

def load_tools_from_dir(tools_dir):
    """从指定目录加载所有工具配置文件"""
    tools = {}
    if not os.path.exists(tools_dir):
        print(f"警告: 工具目录 '{tools_dir}' 不存在")
        return tools
    
    for file_path in Path(tools_dir).glob("*.json"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                tool_data = json.load(f)
                tool_name = file_path.stem.lower()
                
                # 验证必要字段
                if 'help_text' not in tool_data or 'category' not in tool_data:
                    print(f"错误: 工具配置文件 '{file_path}' 格式不完整")
                    continue
                
                tools[tool_name] = {
                    'help_text': tool_data['help_text'],
                    'category': tool_data['category'],
                    'description': tool_data.get('description', '')
                }
        except Exception as e:
            print(f"错误: 加载工具配置文件 '{file_path}' 失败: {str(e)}")
    
    return tools

def main():
    parser = argparse.ArgumentParser(description='安全工具中文帮助信息生成器')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('tool', type=str, nargs='?', help='工具名称')
    group.add_argument('-list', action='store_true', help='列出所有支持的工具')
    parser.add_argument('-tools-dir', type=str, default='/Users/tanglx/Tools/help_CN/tools', 
                        help='工具配置文件目录 (默认: ./tools)')
    args = parser.parse_args()

    # 加载工具信息
    tools = load_tools_from_dir(args.tools_dir)
    
    if not tools:
        print("错误: 未找到任何工具配置文件")
        sys.exit(1)

    if args.list:
        # 按分类分组并排序
        categories = {}
        for tool, info in tools.items():
            category = info['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(tool)
        
        # 按分类名排序输出
        print("支持的工具列表:")
        for category in sorted(categories.keys()):
            print(f"\n[{category}]")
            for tool in sorted(categories[category]):
                desc = tools[tool]['description']
                print(f"  - {tool}{f' ({desc})' if desc else ''}")
    elif args.tool in tools:
        print(tools[args.tool]['help_text'])
    else:
        print(f"错误: 不支持的工具 '{args.tool}'")
        print("\n支持的工具:")
        for category in sorted(categories.keys()):
            print(f"\n[{category}]")
            for tool in sorted(categories[category]):
                print(f"  - {tool}")
        sys.exit(1)

if __name__ == "__main__":
    main()
