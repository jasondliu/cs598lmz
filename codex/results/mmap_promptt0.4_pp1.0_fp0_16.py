import mmap
# Test mmap.mmap()

# Create a file with some data
with open("test_mmap.txt", "wb") as f:
    f.write(b"Hello world!")

# Open the file for reading
with open("test_mmap.txt", "r+b") as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print(mm.readline())  # prints "Hello world!"
    # Update content using slice notation;
    # note that new content must have same size
    mm[6:] = b" world. Hello"
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())  # prints "Hello  world!"
    # close the map
    mm.close()

# Clean up
os.remove("test_mmap.txt")

# Test mmap.mmap()

# Create a file with some data
with open("test_mmap.txt", "wb") as f
