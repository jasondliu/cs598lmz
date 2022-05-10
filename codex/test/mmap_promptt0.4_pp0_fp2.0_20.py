import mmap
# Test mmap.mmap()
# https://docs.python.org/3/library/mmap.html

# open a file for reading
with open("test.txt", "r") as f:
    # memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    # read content via standard file methods
    print(mm.readline())  # prints "Hello Python!"
    mm.seek(0)
    print(mm.readline())  # prints "Hello Python!"
    # read content via slice notation
    print(mm[:5])  # prints "Hello"
    print(mm[6:])  # prints "Python!"
    # update content using slice notation;
    # note that new content must have same size
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())  # prints "Hello Python!"
    # close the map
    mm.close()

# Test mmap.mmap()
# https://docs.python.org
