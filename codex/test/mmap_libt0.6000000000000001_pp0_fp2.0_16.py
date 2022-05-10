import mmap
import sys
import os
import re

def main():
    for filename in sys.argv[1:]:
        with open(filename, 'r') as f:
            s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
