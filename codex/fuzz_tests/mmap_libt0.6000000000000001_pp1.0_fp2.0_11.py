import mmap
import os
import sys
import time

def mmap_file(filename, size):
    if os.path.exists(filename):
        os.remove(filename)
    fd = os.open(filename, os.O_RDWR | os.O_CREAT)
    try:
        os.ftruncate(fd, size)
    except OSError:
        os.close(fd)
        raise
    return mmap.mmap(fd, size)

def main():
    if len(sys.argv) != 4:
        print("Usage: %s <mmap_file> <offset> <data>" % sys.argv[0])
        sys.exit(1)

    filename = sys.argv[1]
    offset = int(sys.argv[2])
    data = sys.argv[3].encode('ascii')
    size = offset + len(data)

    mm = mmap_file(filename, size)
    mm.seek(offset)
    mm.write(data)
    mm.close
