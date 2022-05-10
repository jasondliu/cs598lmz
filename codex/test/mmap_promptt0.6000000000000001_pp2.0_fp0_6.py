import mmap
# Test mmap.mmap()
f = open('/tmp/spam', 'r+b')
map = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
