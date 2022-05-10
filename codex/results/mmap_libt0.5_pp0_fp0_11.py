import mmap
import re
import sys
import time

from util import *

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

def read_file_mmap(filename):
    with open(filename, "r") as f:
        return mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

def read_file_mmap_size(filename):
    with open(filename, "r") as f:
        return mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ), os.path.getsize(filename)

def read_file_mmap_size_offset(filename):
    with open(filename, "r") as f:
        return mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ), os.path.getsize(filename), f.tell()

def read_file_mmap_size_offset_fd(filename):
    f = open(filename, "r")

