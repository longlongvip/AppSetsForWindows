import os
import json

cwd = os.getcwd()
curr_list = os.listdir(cwd)
folder = [i for i in curr_list if (os.path.isfile(i) == False and i == 'venv')]

if folder == []:
    make_venv_cmd = 'py -m venv venv'
    os.system(make_venv_cmd)

update_pip_cmd = 'py -m pip install --upgrade pip'
os.system(update_pip_cmd)

teedoc_install_cmds = [
    'pip install teedoc',
    'pip install -U teedoc'
]

for cmd in teedoc_install_cmds:
    os.system(command=cmd)
