import mmap
# Test mmap.mmap.resize.

import os, sys

fname = 'resize-test'

for size in (0, 1, 100, 200, 400, 800):
    f = open(fname, 'w+')
    f.write('x' * size)
    f.close()
    m = mmap.mmap(f.fileno(), 0)
    m.resize(size)
