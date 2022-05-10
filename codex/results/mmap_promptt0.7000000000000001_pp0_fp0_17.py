import mmap
# Test mmap.mmap()

# works on both Python 2 and Python 3:
def get_int(byteorder='big'):
    return int.from_bytes(f.read(4), byteorder=byteorder)

with open(r"C:\Users\adams\Anaconda3\SPOT\file_io\test_file_io.txt", "r+b") as f:
    # memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print(mm.readline())  # prints "Hello Python!"
    # read content via slice notation
    print(mm[:5])  # prints "Hello"
    # update content using slice notation;
    # note that new content must have same size
    mm[6:] = b" world!\n"
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())  # prints "Hello  world!"
    # close the map
    mm.close()
