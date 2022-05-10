import mmap
import re
import sys

def main(input_file):
    f = open(input_file, 'r')
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    # Find the beginning of the first entry
    entry_start = s.find('#START')
