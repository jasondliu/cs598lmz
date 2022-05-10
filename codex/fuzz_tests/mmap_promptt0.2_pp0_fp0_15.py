import mmap
# Test mmap.mmap()

# Create a file and write a few lines to it
with open('test.txt', 'w+') as f:
    f.write('hello world\n')
    f.write('bye world\n')

# Open the file
with open('test.txt', 'r+') as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print(mm.readline())  # prints "hello world\n"
    # Read content via slice notation
    print(mm[:5])  # prints "hello"
    # Update content using slice notation;
    # note that new content must have same size
    mm[6:] = b'world'
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())  # prints "hello world"
    # close the map
    mm.close()

# Test mmap.mmap()

# Create a file and write a few lines to it

