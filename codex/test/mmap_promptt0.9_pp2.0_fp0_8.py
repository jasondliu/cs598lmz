import mmap
# Test mmap.mmap for large files
# This is important for CloudN.
# But this does not work, 2.6b1 uses the file-based mmap.mmap.

def test1():
    f = open('test.dat', 'wb')
