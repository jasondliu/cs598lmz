import mmap
# Test mmap.mmap()

def run_mmap(fname, size):
    """
    Runs the mmap.mmap() test with the given file and size.
    """
    f = open(fname, 'r+b')
    f.seek(size-1)
    f.write(b'\x00')
    f.close()
    f = open(fname, 'r+b')
    m = mmap.mmap(f.fileno(), size, access=mmap.ACCESS_WRITE)
    m[0:size] = b'\x00' * size
    m.close()
    f.close()

# Test mmap.mmap()

def run_mmap_read(fname, size):
    """
    Runs the mmap.mmap() test with the given file and size.
    """
    f = open(fname, 'r+b')
    f.seek(size-1)
    f.write(b'\x00')
    f.close()
