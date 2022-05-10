import mmap
import os
import re

# split a file into chunks of size n
def split(file, n):
    with open(file, "rb") as f:
        m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        size = os.path.getsize(file)
        chunk_size = size / n
        offset = 0
        while offset < size:
            yield m[offset:offset+chunk_size]
            offset += chunk_size

# get the last n lines of a file
def get_last_lines(file, n):
    with open(file, "rb") as f:
        m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        size = os.path.getsize(file)
        offset = 0
        lines = []
        while offset < size:
            line = m.readline()
            lines.append(line)
            offset += len(line)
