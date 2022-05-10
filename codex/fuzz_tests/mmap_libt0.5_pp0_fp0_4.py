import mmap
import os
import re
import sys

from utils import *

def main():
    if len(sys.argv) < 3:
        print("Usage: %s <input file> <output dir>" % sys.argv[0])
        sys.exit(1)

    in_file = sys.argv[1]
    out_dir = sys.argv[2]

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    with open(in_file, "r+b") as f:
        m = mmap.mmap(f.fileno(), 0)

        # Find the start of the first entry.
        pos = m.find(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
