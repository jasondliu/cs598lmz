import mmap
# Test mmap.mmap(0, 1, "w+")

# This test is for the bug in Python 2.4.2 that causes
# mmap.mmap(0, 1, "w+") to raise an exception.

import mmap

# Create a file and memory map it
with open("test.txt", "wb") as f:
    f.write(b"a")

m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE)

# Try to write to it
m.write(b"b")
