import mmap
# Test mmap.mmap()

# Open file
with open('test.txt', 'r+') as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print(mm.readline())  # prints "Hello Python!\n"
    # Update content using slice notation;
    # note that new content must have same size
    mm[6:13] = b' world'
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())  # prints "Hello  world!\n"
    # close the map
    mm.close()

# Test mmap.mmap()

# Open file
with open('test.txt', 'r+') as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print(mm.readline())  # prints "Hello Python!\n"
   
