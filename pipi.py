# auto add proxy when using pip install.
# Usage:
# set : set proxy for you pip install.
# get : get proxy now.
import sys
import os
import json
config_path = "./config.json"
config = json.load(open(config_path,'r') )
default_proxy = config["proxy"]

def pipi(args):
    cmd_str = 'pip3 ' + " ".join(str(i) for i in args)
    cmd_str += f' -i {default_proxy}'
    print(cmd_str)
    os.system(cmd_str)

def do_fault():
    helper = '''
usage: pipi.py [-h] [--get GET] set
    Auto add proxy when using pip
optional arguments:
    set         [default proxy]
    help        show this help message and exit
    get         get default proxy
'''
    print(helper)

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 1:
        do_fault()
        exit(1)
    if args[0] == 'help': do_fault()
    elif args[0] == 'set':
        if len(args) < 2:
            do_fault()
            exit(1)
        new_proxy = args[1]
        config["proxy"] = new_proxy
        json.dump(config, open(config_path,'w') )
        print("Success to modify proxy.")
    elif args[0] == 'get':
        print(default_proxy)
    else:
        pipi(args)
    