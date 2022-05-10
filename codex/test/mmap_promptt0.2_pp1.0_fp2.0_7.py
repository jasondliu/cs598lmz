import mmap
# Test mmap.mmap.read()

# Create a file
with open('test.txt', 'w+') as f:
    f.write('Hello world')

# Open the file
with open('test.txt', 'r+') as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print(mm.read(11))
    # Read content via slice notation
    print(mm[:5])
    # Update content using slice notation;
    # note that new content must have same size
    mm[6:] = b'world'
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.read(11))
    # close the map
    mm.close()

# Clean up
os.remove('test.txt')

# Test mmap.mmap.write()

# Create a file
with open('test.txt', 'w+') as f:
    f.write('Hello world')

# Open the file
