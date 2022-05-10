import mmap
import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        return 1

    f = open(sys.argv[1], "r+b")
    m = mmap.mmap(f.fileno(), 0)

    for i in range(0, m.size(), 4):
        print(m[i:i+4])
        m[i:i+4] = b'\x00\x00\x00\x00'

    m.close()
    f.close()
    return 0

