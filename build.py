import os
import json

with open('project.json', 'r') as f:
    data = json.load(f)

project_name = data['name']
cmds = [
    f'cd {project_name} && teedoc build',
]

for cmd in cmds:
    print(cmd)
    os.system(cmd)
