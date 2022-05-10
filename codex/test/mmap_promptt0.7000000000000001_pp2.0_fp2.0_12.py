import mmap
# Test mmap.mmap for file-like object

def main():
    # Open file
    f = open('test_data.txt', 'r+')
    # Memory-map the file
    mm = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print('First 10 bytes via read  :', mm.read(10))
    # Read content via slice notation
    print('First 10 bytes via slice :', mm[:10])
    # Update content using slice notation;
    # note that new content must have same size
    # as original content
    mm[0:11] = b'Hello World'
    # ... and read again using standard file methods
    mm.seek(0)
    print('First 10 bytes via read  :', mm.read(10))
    # Close the map
    mm.close()
    # close the file
    f.close()


