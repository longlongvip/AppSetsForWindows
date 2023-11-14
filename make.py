import os

dir_name = input()

if dir_name == "":
    print("请想好项目名字")
else:
    os.mkdir(dir_name)
    cmd = f"cd {dir_name} && teedoc init"
    os.system(cmd)
