import mmap
# Test mmap.mmap.readline()

# Create a file
with open("test_mmap_readline.txt", "w+") as f:
    f.write("Hello Python!\n")

# Open the file
with open("test_mmap_readline.txt", "r+") as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print(mm.readline())
    # Read content via slice notation
    print(mm[:5])
    # Update content using slice notation;
    # note that new content must have same size
    mm[6:] = " world!\n"
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())
    # close the map
    mm.close()
