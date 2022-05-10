import mmap
# Test mmap.mmap
#
# This test is intended to be run from the root directory of the
# source tree.

import mmap
import os

try:
    import ctypes
except ImportError:
    ctypes = None

def main():
    # Create a file to test with
    filename = 'mmap_mmap.dat'
    fd = os.open(filename, os.O_CREAT | os.O_RDWR)
    os.write(fd, '\x00' * 1024)
    os.close(fd)

    # Open the file in read-write mode
    f = open(filename, 'r+')
    m = mmap.mmap(f.fileno(), 1024)

    # Simple sanity tests
    assert len(m) == 1024
    assert m.size() == 1024

    # Modify a few bytes
    m[0] = 'a'
    m[2] = 'b'

    # Check that the modifications went through
    f.seek(0)
    assert f.read(1) == 'a'
