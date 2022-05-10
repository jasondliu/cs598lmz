import mmap
import sys
import os
import re

def main():
    for filename in sys.argv[1:]:
        with open(filename, 'r') as f:
            s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            if s.find('\x50\x4b\x03\x04') != -1:
                print filename

if __name__ == '__main__':
    main()
