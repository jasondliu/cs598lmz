import mmap
# Test mmap.mmap
# https://docs.python.org/3/library/mmap.html

# TODO: write a small test code of mmap.mmap
# TODO: read the code and the docs
# TODO: try to understand what this code is doing
# TODO: try to understand what mmap is doing

# TODO: try to understand what this code is doing
with open("tmp.txt", "wb") as f:
    f.write(b"This is a test")

with open("tmp.txt", "r+b") as f:
    # memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print(mm.readline())  # prints "This is a test"
    # read content via slice notation
    print(mm[:5])  # prints "This "
    # update content using slice notation;
    # note that new content must have same size
    mm[6:] = b"was a test"
    # ... and read again using standard file methods
