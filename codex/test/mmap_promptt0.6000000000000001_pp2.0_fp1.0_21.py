import mmap
# Test mmap.mmap.write_byte()
# Write a byte to a given position in the mmap'ed file.
# The byte is specified as an integer in the range 0-255.

# The current position is not changed.

import os, mmap

# write a simple example file
with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

with open("hello.txt", "r+b") as f:
    # memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print(mm.readline())  # prints "Hello Python!"
    # read content via slice notation
    print(mm[:5])  # prints "Hello"
    # update content using slice notation;
    # note that new content must have same size
    mm[6:] = b" world!\n"
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())  # prints "Hello 
