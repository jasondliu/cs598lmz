import mmap
# Test mmap.mmap.read()

# Create a file
with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

# Open the file
with open("hello.txt", "r+b") as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print(mm.readline())  # prints "Hello Python!"
    # Read content via slice notation
    print(mm[:5])  # prints "Hello"
    # Update content using slice notation;
    # note that new content must have same size
    mm[6:] = b" world!\n"
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())  # prints "Hello  world!"
    # close the map
    mm.close()

# Test mmap.mmap.write()

# Create a file
with open("hello.txt", "wb") as f:
    f
