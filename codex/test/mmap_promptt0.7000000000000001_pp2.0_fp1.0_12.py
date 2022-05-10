import mmap
# Test mmap.mmap.__new__ and mmap.mmap.__init__
with open('berlin.jpg', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.close()
# Test mmap.mmap.__new__ and mmap.mmap.__init__
with open('berlin.jpg', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    m.close()
# Test mmap.mmap.__init__
m = mmap.mmap(-1, 0)
m.close()
# Test mmap.mmap.__init__
