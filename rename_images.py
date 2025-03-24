# import os

# def replace_spaces_with_underscores(directory):
#     """
#     递归地将给定目录及其子目录中的所有图片文件名中的空格替换为下划线。

#     Args:
#         directory (str): 要处理的目录路径。
#     """
#     for root, _, files in os.walk(directory):
#         for filename in files:
#             # 检查文件是否为图片（可以根据需要扩展图片类型列表）
#             if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
#                 new_filename = filename.replace(' ', '_')
#                 if new_filename != filename:
#                     old_filepath = os.path.join(root, filename)
#                     new_filepath = os.path.join(root, new_filename)
#                     os.rename(old_filepath, new_filepath)

# # 获取当前工作目录
# current_directory = os.getcwd()

# # 调用函数处理当前目录及其子目录
# replace_spaces_with_underscores(current_directory)


import os

def replace_non_segmented_extensions(directory):
    """
    递归地将给定目录及其子目录中的所有文件名中，不含最后一个 '.' 的部分替换为下划线。

    Args:
        directory (str): 要处理的目录路径。
    """
    for root, _, files in os.walk(directory):
        for filename in files:
            if '.' in filename:
                # 找到最后一个 '.' 的位置
                last_dot_index = filename.rfind('.')
                # 提取文件名和扩展名
                name_part = filename[:last_dot_index]
                extension_part = filename[last_dot_index:]
                # 将文件名部分中的空格替换为下划线
                new_name_part = name_part.replace(' ', '_').replace('.', '_')
                # 组合成新的文件名
                new_filename = new_name_part + extension_part
                # 如果新文件名与旧文件名不同，则重命名文件
                if new_filename != filename:
                    old_filepath = os.path.join(root, filename)
                    new_filepath = os.path.join(root, new_filename)
                    os.rename(old_filepath, new_filepath)
            else:
                # 文件名中没有 '.'，直接替换所有空格
                new_filename = filename.replace(' ', '_')
                if new_filename != filename:
                    old_filepath = os.path.join(root, filename)
                    new_filepath = os.path.join(root, new_filename)
                    os.rename(old_filepath, new_filepath)

# 获取当前工作目录
current_directory = os.getcwd()

# 调用函数处理当前目录及其子目录
replace_non_segmented_extensions(current_directory)