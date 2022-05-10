import mmap
# Test mmap.mmap(0, 1).move(1, 2, 3)

from mmap import *
import os

# Create an empty file
with open(TESTFN, "w+b") as f:
    pass

with open(TESTFN, "r+b") as f:
    m = mmap(f.fileno(), 1024)
    m.move(1, 2, 3)
    assert m[1:4] == b'\x00\x00\x00'
    m[1:4] = b'foo'
    assert m[1:4] == b'foo\x00'
    m.move(1, 2, 3)
    assert m[1:4] == b'foo\x00'
    m.move(1, 2, 3)
    assert m[1:4] == b'foo\x00'
    m.move(2, 3, 1)
    assert m[1:4] == b'\x00oo\x00'
    m.move(2, 3, 1)
    assert m[1:4]
