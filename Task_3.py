import os
from pprint import pprint

files_list = ['1.txt', '2.txt', '3.txt']
line_count_list = [] #
dict_texts = {}
dict_files = {}
for file in files_list:
    path = os.path.join(os.getcwd(), file)
    with open(path, encoding='utf-8') as text:
        text_text = text.readlines()
        line_count = len(text_text)
        line_count_list.append(line_count)
        dict_texts.update({line_count: text_text})
        dict_files.update({line_count: file})
path_write = os.path.join(os.getcwd(), 'sorted_list.txt')
with open(path_write, "a", encoding='utf-8') as file:
    for count in sorted(line_count_list):
        file.write(dict_files[count] + "\n")
        file.write(str(sorted(line_count_list).index(count) + 1) + "\n")
        for line in dict_texts[count]:
            file.write(line.strip())
            file.write('\n')
