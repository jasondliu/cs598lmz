import mmap
# Test mmap.mmap
from mmap import mmap
import sys
import os
from tempfile import TemporaryFile

print "Testing mmap.mmap..."
testfile = "test.mmap"

try:
    size = 1000000
    f = open(testfile, "wb+")
    f.write('\0'*size)
    f.seek(0)
    m = mmap(f.fileno(), size)
    m[0] = 'a'
    m.seek(0)
    assert m.read(1) == 'a'
    assert m.tell() == 1
    m.seek(0, 0)
    assert m.tell() == 0
    m.seek(10, 1)
    assert m.tell() == 10
    m.seek(-1, 2)
    assert m.tell() == size-1
    m.close()
    f.close()
    os.unlink(testfile)
except SystemError, msg:
    print "Caught system error:", msg
    print "Probably no memory on machine."
    print "Test", sys.
