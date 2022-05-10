import socket
import sys
import os
import re
import argparse

def processCommand(command):
    command = re.fienall(r"^\s*(\w+)\s*(.*)", command)
    if len(command) == 3 and command[0].startswith('PWD'):
        try:
            os.getcwd()
            print(cwd)
        except Exception as e:
            print(e)
    elif len(command) == 2 and command[0].startswith('LS'):
        try:
            os.listdir()
            print(dir)
        except Exception as e:
            print(e)
    elif len(command) == 3 and command[0].startswith('CD'):
        try:
            os.chdir(dir)
            print(dir)
        except Exception as e:
            print(e)
