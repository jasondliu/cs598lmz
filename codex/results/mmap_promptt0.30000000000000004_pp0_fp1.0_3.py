import mmap
# Test mmap.mmap(fileno, length)

with open("foo.txt", "wb") as f:
    f.write(b"Hello Python!\n")

with open("foo.txt", "r+b") as f:
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
    print(mm.readline())  # prints "Hello  world!"
    # close the map
    mm.close()

# Test mmap.mmap(fileno, length, access=ACCESS_WRITE)

with open("bar.txt", "wb") as f:
    f.
