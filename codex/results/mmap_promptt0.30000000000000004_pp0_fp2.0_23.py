import mmap
# Test mmap.mmap()

# Create a file with some data
with open('data.txt', 'w') as f:
    f.write('Hello, world!')

# Open the file for reading
with open('data.txt', 'r') as f:
    # Memory-map the file, size 0 means whole file
    m = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print(m.readline())
    # Read content via slice notation
    print(m[:5])
    # Update content using slice notation;
    # note that new content must have same size
    m[6:] = b'world'
    # ... and read again using standard file methods
    m.seek(0)
    print(m.readline())
    # close the map
    m.close()

# Clean up
os.remove('data.txt')

# Test mmap.mmap()

# Create a file with some data
with open('data.txt', 'w') as f:
    f.write('Hello, world!')

#
