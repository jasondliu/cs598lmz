import mmap
# Test mmap.mmap()
filename = 'test.txt'
with open(filename, 'r+') as f:
    # Memory-map the file, size 0 means whole file
    m = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print(m.readline())  # prints "Hello Python!"
    # Read content via slice notation
    print(m[:5])  # prints "Hello"
    # Update content using slice notation;
    # note that new content must have same size
    m[6:] = 'world!\n'
    # ... and read again using standard file methods
    m.seek(0)
    print(m.readline())  # prints "Hello world!"
    # close the map
    m.close()

# Test mmap.mmap() using a file descriptor
with open(filename, 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.readline())  # prints "Hello world!"
    # close the map
    m.close()


