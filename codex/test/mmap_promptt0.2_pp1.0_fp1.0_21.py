import mmap
# Test mmap.mmap()

# Create a memory-mapped file
with open("hello.txt", "w+b") as f:
    # Write a few bytes to the file
    f.write(b"Hello Python!\n")

    # Create a memory-map to the file, size 0 means whole file
    m = mmap.mmap(f.fileno(), 0)

    # Read content via standard file methods
    print(m.readline())

    # Update content using slice notation;
    # note that new content must have same size
    m[6:13] = b" world"

    # See what we have now
    m.seek(0)
    print(m.readline())

    # Close the map and file
    m.close()

