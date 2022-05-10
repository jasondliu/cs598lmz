import mmap
import numpy as np
import time
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: %s <file>" % sys.argv[0])
        sys.exit(1)

    file = sys.argv[1]
    fd = os.open(file, os.O_RDONLY)
    size = os.path.getsize(file)

    # memory-map the file, size 0 means whole file
    map = mmap.mmap(fd, size, prot=mmap.PROT_READ)

    # read content via standard file methods
    print(map.readline())  # prints "Hello Python!"

    # read content via slice notation
    print(map[:5])  # prints "Hello"

    # update content using slice notation;
    # note that new content must have same size
    #map[6:] = " world!\n"

    # ... and read again using standard file methods
    #map.seek(0)
    #print(map.readline())  #
