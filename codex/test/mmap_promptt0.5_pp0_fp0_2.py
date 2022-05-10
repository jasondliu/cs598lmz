import mmap
# Test mmap.mmap(-1, length)

# Create a file to mmap
with open("test_mmap_mmap_negative_length.txt", "wb") as f:
    f.write("Hello, World!")

# Open the file for reading
with open("test_mmap_mmap_negative_length.txt", "r+b") as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print(mm.readline())  # prints "Hello Python!"
    # Update content using slice notation;
    # note that new content must have same size
    mm[6:12] = " world"
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())  # prints "Hello  world!"
    # close the map
