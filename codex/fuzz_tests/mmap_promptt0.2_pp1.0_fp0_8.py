import mmap
# Test mmap.mmap()

# Create a file and write some data to it
with open('test.txt', 'w+') as f:
    f.write('Hello World')

# Open the file in read-only mode
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
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())
    # close the map
    mm.close()

# Clean up
os.remove('test.txt')

# Test mmap.mmap()

# Create a file and write some data to it
with open('test.txt', 'w+') as f:
    f.write
