import mmap
# Test mmap.mmap() and mmap.map_size()
with open('some_file', 'r') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    all_chars = set(chr(i) for i in xrange(256))
    found = set(c for c in m)
    # No need to check whether m.close() is needed.
    # mmap.mmap objects are context managers, and the close() method is 
    # automatically called for you when exiting the with block.
    print found == all_chars
