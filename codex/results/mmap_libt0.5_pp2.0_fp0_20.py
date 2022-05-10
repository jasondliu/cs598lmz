import mmap
import sys
import re

def mmap_file(filename):
    fd = os.open(filename, os.O_RDONLY)
    return mmap.mmap(fd, 0, access=mmap.ACCESS_READ)


def get_file_lines(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    return lines


def get_file_lines_mmap(filename):
    f = mmap.mmap(open(filename, 'r').fileno(), 0, access=mmap.ACCESS_READ)
    lines = f.readlines()
    f.close()
    return lines


def get_file_lines_mmap_read(filename):
    f = mmap.mmap(open(filename, 'r').fileno(), 0, access=mmap.ACCESS_READ)
    lines = []
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line)
    f.close()
    return lines
