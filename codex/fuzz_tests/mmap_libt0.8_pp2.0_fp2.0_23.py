import mmap
import os
import sys

# py2/3 compat
if sys.version_info[0] == 2:
    range = xrange

def mmap_find(fname, substr):
    with open(fname, "r+") as f:
        mm = mmap.mmap(f.fileno(), 0)
    pos = 0
    while True:
        pos = mm.find(substr, pos)
        if pos == -1:
            break
        yield pos
        pos += len(substr)

def get_offsets(fname):
    offsets = []
    for match in mmap_find(fname, b"\n\n"):
        offsets.append(match)
    return offsets


def get_last_entry(fname, offset):
    with open(fname, "r+") as f:
        mm = mmap.mmap(f.fileno(), 0)
        mm.move(0, offset, 2)
        mm.seek(0)
        line = mm.readline()
        if not line:
