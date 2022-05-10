import mmap
# Test mmap.mmap() with anonymous maps, and verify that the
# mapped range can be written to.

with open(os.devnull, 'w') as f:
    m = mmap.mmap(f.fileno(), 1)
    m[:] = b'a'
    m.close()
