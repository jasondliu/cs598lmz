import mmap
# Test mmap.mmap()

# Open file for reading
with open("lorem.txt", "r") as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    # Read content via standard file methods
    print(mm.readline())  # b'Lorem ipsum dolor sit amet, consectetur\n'
    # Read content via slice notation
    print(mm[:5])  # b'Lorem'
    # Update content using slice notation;
    # note that new content must have same size
    mm[6:11] = b"python"
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())  # b'Lorem python dolor sit amet, consectetur\n'
    # close the map
    mm.close()

# Open file for writing
