import mmap
# Test mmap.mmap()
#
# Create a memory-map to an int array.
#
# Note that for read-write maps, modifications to the array
# data are not written through to the file unless sync() or
# close() is called.
#
# To create a map for a file that does not exist, use the
# `os.O_CREAT` flag in the `open()` call.
#
# It is not possible to resize a file using a memory-mapped
# object - any attempt to resize the file before the mmap
# object is closed will result in a `ValueError`.

import os
import mmap
import contextlib

# Write a simple example file
with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

with open("hello.txt", "r+b") as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print(mm.readline())  # prints b"Hello Python
