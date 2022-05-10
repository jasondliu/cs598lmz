import mmap
# Test mmap.mmap()

# Create a file with some data
with open('test.txt', 'w+') as f:
    f.write('Hello world')

# Open the file for reading
with open('test.txt', 'r') as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print(mm.readline())
    # Read content via slice notation
    print(mm[:5])
    # Update content using slice notation;
    # note that new content must have same size
    mm[6:] = 'WORLD'
    mm.seek(0)
    print(mm.readline())
    # Close the map
    mm.close()

# Open the file for writing
with open('test.txt', 'r+') as f:
    # Memory-map the file, size 0 means whole file, read/write
    mm = mmap.mmap(f.fileno(), 0)
