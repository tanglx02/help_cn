import json
import os

def clear_screen():
    """清屏函数，提升用户体验"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print("=" * 50)
    print("       安全工具模板创建程序")
    print("=" * 50)
    print("\n请选择工具分类：")
    
    # 定义分类选项
    categories = [
        "信息收集工具", "漏洞扫描工具", "Web 应用测试工具", 
        "密码破解工具", "网络嗅探与欺骗工具", "漏洞利用框架",
        "无线安全工具", "社会工程学工具", "后渗透与权限提升工具",
        "硬件与物联网渗透工具", "移动应用安全工具"
    ]
    
    # 显示分类选项
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    # 获取用户选择
    while True:
        try:
            choice = int(input("\n请输入分类编号 (1-11): "))
            if 1 <= choice <= len(categories):
                selected_category = categories[choice - 1]
                break
            else:
                print("输入无效，请选择1到11之间的数字！")
        except ValueError:
            print("请输入有效的数字！")
    
    # 获取描述信息
    description = input("\n请输入工具描述: ")
    
    # 获取帮助文本
    print("\n请输入帮助文本 (输入空行结束):")
    help_lines = []
    while True:
        line = input()
        if not line:
            break
        help_lines.append(line)
    help_text = "\n".join(help_lines)
    
    # 构建JSON数据
    template = {
        "category": selected_category,
        "description": description,
        "help_text": help_text
    }
    
    # 输出生成的JSON
    print("\n" + "=" * 50)
    print("生成的JSON模板:")
    print(json.dumps(template, ensure_ascii=False, indent=4))
    print("=" * 50)
    
    # 保存到指定路径
    save_path = "/Users/tanglx/Tools/help_CN/tools"
    
    # 确保目录存在
    os.makedirs(save_path, exist_ok=True)
    
    # 获取自定义文件名
    filename = input("\n请输入自定义文件名 (无需扩展名): ")
    
    # 规范化文件名
    filename = filename.strip()
    if not filename:
        # 如果用户未输入文件名，使用默认名称
        filename = "tool_template"
    
    # 添加JSON扩展名
    if not filename.endswith('.json'):
        filename += '.json'
    
    # 构建完整路径
    full_path = os.path.join(save_path, filename)
    
    try:
        with open(full_path, 'w', encoding='utf-8') as f:
            json.dump(template, f, ensure_ascii=False, indent=4)
        print(f"\n已保存到: {full_path}")
    except Exception as e:
        print(f"\n保存文件时出错: {e}")
        # 提供手动保存选项
        save_manual = input("\n是否手动指定保存路径? (y/n): ").lower()
        if save_manual == 'y':
            try:
                filename = input("请输入文件名: ")
                if not filename.endswith('.json'):
                    filename += '.json'
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(template, f, ensure_ascii=False, indent=4)
                print(f"已保存到 {filename}")
            except Exception as e:
                print(f"保存文件时出错: {e}")

if __name__ == "__main__":
    main()

