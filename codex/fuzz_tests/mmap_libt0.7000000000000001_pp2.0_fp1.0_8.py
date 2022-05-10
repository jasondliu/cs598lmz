import mmap
import sys
import os
from random import randint
from string import ascii_lowercase

from pwn import *

# context.log_level = 'debug'

def get_flag():
    with open("flag", "r") as f:
        flag = f.read()
    return flag

def get_puzzle_path(n, rand):
    return "puzzle/puzzle{}_{}".format(n, rand)

def get_puzzle_file(n, rand):
    path = get_puzzle_path(n, rand)
    if os.path.isfile(path):
        return open(path, "r")
    else:
        return None

def get_puzzle_data(p):
    f = get_puzzle_file(p.n, p.rand)
    if f:
        return mmap.mmap(f.fileno(), 0, access = mmap.ACCESS_READ)
    else:
        return None

def generate_random_string(length):
    return ''.join(choice
