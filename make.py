import json
import os, re

dir_name = input("请输入项目名字：")

while dir_name == "":
    print("请想好项目名字, 项目创建后, 项目名不可更改, 切记!切记!")
    dir_name = input("请输入项目名字：")

while re.match(pattern=r'\w+', string=dir_name, flags=re.ASCII) == None:
    print("项目名字只包含52个英文字母和10个数字, 切记!切记!")
    dir_name = input("请输入项目名字：")

create_flag = input("要创建项目吗？ [Yes] Y, [No] N：")
if create_flag == 'Y':
    content = {'name': dir_name}
    with open('project.json', mode='r', encoding='utf-8') as f:
        json.dump(content, f)
    os.mkdir(dir_name)
    cmd = f"cd {dir_name} && teedoc init && teedoc install"
    os.system(cmd)
