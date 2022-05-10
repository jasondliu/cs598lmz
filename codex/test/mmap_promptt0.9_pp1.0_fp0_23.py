import mmap
# Test mmap.mmap constructor; create 7-byte-long read-only map
size = 7
# Create a zero filled buffer
with open(path, 'r+b') as f:
    buf = mmap.mmap(f.fileno(), size, flags=mmap.MAP_SHARED,
                    prot=mmap.PROT_READ)
