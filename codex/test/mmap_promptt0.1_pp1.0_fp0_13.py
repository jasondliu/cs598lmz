import mmap
# Test mmap.mmap.read_byte()

# Create a file
with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

# Open the file
with open("hello.txt", "r+b") as f:
    # Memory-map the file, size 0 means whole file
    m = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print(m.readline())  # prints "Hello Python!"
    # Read content via slice notation
    print(m[:5])  # prints "Hello"
    # Update content using slice notation;
    # note that new content must have same size
    m[6:] = b" world!\n"
    # ... and read again using standard file methods
    m.seek(0)
    print(m.readline())  # prints "Hello  world!"
    # close the map
    m.close()

# Clean up
os.unlink("hello.txt")
