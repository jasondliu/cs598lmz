import mmap
import re
import sys
import os

def start_server():
    os.system('python3 server.py')

def start_client():
    os.system('python3 client.py')

def main():
    if sys.argv[1] == 'server':
        start_server()
    elif sys.argv[1] == 'client':
        start_client()
    else:
        print('Unknown command')

