import mmap
# Test mmap.mmap.read_byte
with open('/dev/null', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.read_byte()
# Test mmap.mmap.readline
with open('/dev/null', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.readline()
# Test mmap.mmap.readlines
with open('/dev/null', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.readlines()
# Test mmap.mmap.seek
with open('/dev/null', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
# Test mmap.mmap.tell
with open('/dev/null', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.tell()
# Test
