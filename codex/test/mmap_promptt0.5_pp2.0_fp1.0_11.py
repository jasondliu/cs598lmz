import mmap
# Test mmap.mmap.readline()

with open(sys.argv[1], 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
