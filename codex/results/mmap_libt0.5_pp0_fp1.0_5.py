import mmap
import sys
import re

def find_pattern(pattern, filename):
    with open(filename, "r+b") as f:
        data = mmap.mmap(f.fileno(), 0)
        for m in re.finditer(pattern, data):
            print("Found pattern at: {0}".format(m.start()))

if __name__ == "__main__":
    if len(sys.argv) == 3:
        pattern = sys.argv[1]
        filename = sys.argv[2]
        find_pattern(pattern, filename)
    else:
        print("Usage: python mmap_regex.py [pattern] [filename]")
