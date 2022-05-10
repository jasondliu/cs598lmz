import mmap
# Test mmap.mmap.read_byte()

# Create a file
with open('testmmap.txt', 'wb') as f:
    f.write(b'0123456789abcdef')

# Open the file for reading
with open('testmmap.txt', 'r+b') as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read the content via standard file methods
    print(mm.read_byte())
    print(mm.read_byte())
    # Read the content via slice notation
    print(mm[:])
    # Update content using slice notation;
    # note that new content must have same size
    mm[9:] = b'ABCDEFGHIJKLMNOP'
    mm.seek(0)
    print(mm.read_byte())
    print(mm.read_byte())
    print(mm.read_byte())
    print(mm.read_byte())
    print(mm.read_byte())
    print(mm.read_byte())
   
