import mmap
# Test mmap.mmap(0, 0)
with open(os.devnull, 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.close()

# Test mmap.mmap(-1, 0)
with open(os.devnull, 'r+b') as f:
    m = mmap.mmap(-1, 0)
    m.close()

# Test mmap.mmap(0, 0, access=mmap.ACCESS_READ)
with open(os.devnull, 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    m.close()

# Test mmap.mmap(-1, 0, access=mmap.ACCESS_READ)
