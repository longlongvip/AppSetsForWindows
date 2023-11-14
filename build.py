import os

cmds = [
    'cd app && teedoc build',
]

for cmd in cmds:
    print(cmd)
    os.system(cmd)
