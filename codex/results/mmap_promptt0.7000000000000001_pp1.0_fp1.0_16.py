import mmap
# Test mmap.mmap
with open("test.txt", "r+") as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(1024)
    raw = m.read(1024)

# Test mmap.mmap with offset and length
with open("test.txt", "r+") as f:
    m = mmap.mmap(f.fileno(), 0, offset=0, length=1024)
    m.resize(1024)
    raw = m.read(1024)

# Test mmap.mmap with length
with open("test.txt", "r+") as f:
    m = mmap.mmap(f.fileno(), 1024)
    m.resize(1024)
    raw = m.read(1024)

# Test mmap.mmap with offset = -1
with open("test.txt", "r+") as f:
    m = mmap.mmap(f.fileno(), 0, offset=-1)
    m.resize(1024)
    raw = m.read(1024)

