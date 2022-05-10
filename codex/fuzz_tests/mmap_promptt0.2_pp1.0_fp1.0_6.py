import mmap
# Test mmap.mmap
# https://docs.python.org/3/library/mmap.html

# Create a file
with open('test.txt', 'w') as f:
    f.write('Hello world!')

# Open the file
with open('test.txt', 'r+') as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print(mm.readline())  # prints "Hello world!"
    # Read content via slice notation
    print(mm[:5])  # prints "Hello"
    # Update content using slice notation;
    # note that new content must have same size
    mm[6:] = b'world!'
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())  # prints "Hello world!"
    # close the map
    mm.close()

# Unlink the file
os.unlink('test.txt')

# Create a file
with open('test.
