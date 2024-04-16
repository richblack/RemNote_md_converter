# -*- coding: utf-8 -*-

import os
import re
import tkinter as tk
from tkinter import filedialog

"""## 處理標準的 MD 格式"""

def convert_format(md):
    # 處理標題
    md = re.sub(r'^(\s*)- (.+) #h1', r'\1# \2', md, flags=re.MULTILINE)
    md = re.sub(r'^(\s*)- (.+) #h2', r'\1## \2', md, flags=re.MULTILINE)
    md = re.sub(r'^(\s*)- (.+) #h3', r'\1### \2', md, flags=re.MULTILINE)
    md = re.sub(r'^(\s*)- (.+) #h4', r'\1#### \2', md, flags=re.MULTILINE)
    md = re.sub(r'^(\s*)- (.+) #h5', r'\1##### \2', md, flags=re.MULTILINE)
    md = re.sub(r'^(\s*)- (.+) #h6', r'\1###### \2', md, flags=re.MULTILINE)

    # 處理程式碼區塊
    md = re.sub(r'^(\s*)- ```(.+)```', r'\1```\2```', md, flags=re.MULTILINE)

    # 刪除梗概行
    md = re.sub(r'^(\s*)- (.+) #OutLine.*\n', '', md, flags=re.MULTILINE)

    # 移除非列表、非表格的 '-'
    md = re.sub(r'^(\s*)- (.+)(?!.*#(ul|ol|ListToTable))$', r'\1\2', md, flags=re.MULTILINE)

    # 移除其他 RemNote 特定的標記, 但保留需要 Lua 處理的格式標記
    md = re.sub(r' #(?!NoSpace|ImageCaption|TableCaption|Right|Centered|Justified|distributed)\w+', '', md)

    # 移除非列表項目的縮排
    lines = md.split('\n')
    converted_lines = []
    for line in lines:
        if not re.match(r'^(\s*)([-*]|\d+\.) ', line):
            line = line.lstrip()
        converted_lines.append(line)
    md = '\n'.join(converted_lines)

    return md

"""## 處理列表"""

def convert_lists(remnote_md):
    lines = remnote_md.split('\n')
    converted_lines = []
    list_indent = None
    list_type = None
    ol_count = {}

    for i, line in enumerate(lines):
        if re.search(r'^(\s*)- (.+) #(ul|ol)', line):
            # 如果前一個列表沒有空行,在前一個列表的最後添加一個空行
            if list_indent is not None:
                converted_lines.append('')
            # 列表首行
            list_type = re.search(r'^(\s*)- (.+) #(ul|ol)', line).group(3)
            indent = re.match(r'^(\s*)', line).group(1)
            list_indent = len(indent)
            if list_type == 'ol':
                ol_count = {0: 1}  # 將縮進量初始化為 0
            converted_line = re.sub(r' #(ul|ol)', '', line)  # 只刪除 #ul 和 #ol 標籤
            converted_lines.append(converted_line)
        elif list_indent is not None:
            if line.startswith(' ' * (list_indent + 2)):
                # 列表項目
                relative_indent = len(re.match(r'^(\s*)', line).group(1)) - list_indent - 2
                content = re.sub(r'^(\s*)- (.+)', r'\2', line).strip()
                if list_type == 'ol':
                    count = ol_count.get(relative_indent, 1)
                    converted_line = '{}{}.{}'.format('  ' * (relative_indent // 2), count, content)
                    ol_count[relative_indent] = count + 1
                else:
                    converted_line = '{}{}'.format('  ' * (relative_indent // 2), '* ' + content)
                converted_lines.append(converted_line)
            else:
                # 列表結束,在最後添加一個空行
                converted_lines.append('')
                list_indent = None
                list_type = None
                ol_count = {}
                converted_lines.append(line)
        else:
            # 一般內文
            converted_lines.append(line)

    # 如果最後一個列表項目後面沒有空行,在最後添加一個空行
    if list_indent is not None:
        converted_lines.append('')

    remnote_md = '\n'.join(converted_lines)
    return remnote_md

"""## 處理表格"""

def convert_list_to_table(md):
    lines = md.split('\n')
    converted_lines = []
    table_data = []
    in_table = False
    table_indent = 0
    for i, line in enumerate(lines):
        if re.search(r'^(\s*)(.+) #ListToTable', line):
            # 表格首行
            in_table = True
            table_indent = len(re.search(r'^(\s*)', line).group(1))
            converted_lines.append(re.sub(r'^(\s*)(.+) #ListToTable', r'\1\2', line))
        elif in_table:
            current_indent = len(re.search(r'^(\s*)', line).group(1))
            if current_indent <= table_indent:
                # 當前行的縮進小於等於表格首行,表格結束
                in_table = False
                # 生成表格
                if table_data:
                    num_cols = len(table_data) // 2
                    table_header = '| ' + ' | '.join([table_data[i] for i in range(num_cols)]) + ' |'
                    table_separator = '|' + '|'.join(['-' * (len(table_data[i]) + 2) for i in range(num_cols)]) + '|'
                    table_rows = '| ' + ' | '.join([table_data[i] for i in range(num_cols, len(table_data))]) + ' |'
                    table = [table_header, table_separator, table_rows]
                    converted_lines.extend(table)
                table_data = []
            else:
                # 表格行
                cols = [col.strip() for col in line.strip().split('-') if col.strip()]
                table_data.extend(cols)
        if not in_table:
            # 一般內文或列表項目
            converted_lines.append(line)
    # 處理最後一個表格
    if in_table and table_data:
        num_cols = len(table_data) // 2
        table_header = '| ' + ' | '.join([table_data[i] for i in range(num_cols)]) + ' |'
        table_separator = '|' + '|'.join(['-' * (len(table_data[i]) + 2) for i in range(num_cols)]) + '|'
        table_rows = '| ' + ' | '.join([table_data[i] for i in range(num_cols, len(table_data))]) + ' |'
        table = [table_header, table_separator, table_rows]
        converted_lines.extend(table)
    md = '\n'.join(converted_lines)
    return md

"""## 按照順序執行程式"""

def convert_remnote_md_to_md(remnote_md):
    md = convert_lists(remnote_md)
    md = convert_list_to_table(md)
    md = convert_format(md)
    return md

"""## 從桌面選擇原 MD 檔"""

def select_file():
    root = tk.Tk()
    # root.withdraw()  # 隱藏主窗口
    file_path = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md")])
    return file_path

"""## 執行"""

def main():
    # 使用文件選擇器選擇要轉換的文件
    input_file = select_file()

    if input_file:
        print(f"選擇的文件: {input_file}")
        # 讀取文件內容
        with open(input_file, 'r', encoding='utf-8') as file:
            remnote_md = file.read()

        # 轉換文件內容
        md = convert_remnote_md_to_md(remnote_md)

        # 生成轉換後的文件名
        output_file = os.path.splitext(input_file)[0] + '_converted.md'

        # 將轉換後的內容寫入文件
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(md)

        print(f"轉換完成。轉換後的文件已保存為: {output_file}")
    else:
        print("未選擇文件,轉換已取消。")

if __name__ == '__main__':
    main()
