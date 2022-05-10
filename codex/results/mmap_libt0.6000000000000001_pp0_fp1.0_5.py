import mmap
import random
import sys
import time

def main():
    # make sure we have enough command line arguments
    if len(sys.argv) < 3:
        print('usage: %s <file-to-mmap> <file-to-write-to>' % sys.argv[0])
        return 1

    # open the file to mmap
    try:
        fd = os.open(sys.argv[1], os.O_RDWR)
    except OSError as e:
        print('failed to open "%s" for writing: %s' % (sys.argv[1], str(e)))
        return 1

    # mmap the file
    try:
        mm = mmap.mmap(fd, 0, access=mmap.ACCESS_WRITE)
    except ValueError as e:
        print('failed to mmap "%s": %s' % (sys.argv[1], str(e)))
        return 1

    # open the file to write to
    try:
        f = open(sys.argv[2
