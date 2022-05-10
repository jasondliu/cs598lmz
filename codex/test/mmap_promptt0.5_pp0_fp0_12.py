import mmap
# Test mmap.mmap(fileno, length, access=mmap.ACCESS_WRITE)

# Create the file
size = 1024
with open('hello.txt', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

# Open the file
with open('hello.txt', 'r+b') as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print(mm.readline())
    # read content via slice notation
    print(mm[:5])
    # update content using slice notation;
    # note that new content must have same size
    mm[6:] = b'world'
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())
    # close the map
    mm.close()

# Test mmap.mmap(fileno, length, access=mmap.ACCESS_READ)
