import mmap
# Test mmap.mmap.read()

# Create a file
with open('test.txt', 'w+b') as f:
    f.write(b'0123456789abcdef')

# Open the file
with open('test.txt', 'r+b') as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print(mm.read(4))
    print(mm.read(4))
    print(mm.read(4))
    print(mm.read(4))
    # Read content via slice notation
    print(mm[4:8])
    # Update content using slice notation;
    # note that new content must have same size
    mm[4:8] = b'XXXX'
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.read(4))
    print(mm.read(4))
    print(mm.read(4))
    print(mm.read(4))
   
