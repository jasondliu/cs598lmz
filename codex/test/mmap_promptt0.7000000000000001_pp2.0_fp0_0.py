import mmap
# Test mmap.mmap with a file larger than 4GB

# First try with a single mmap
with open('test.dat', 'wb') as f:
    f.seek(4*1024**3 - 1)
    f.write(b'\0')

with open('test.dat', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(4*1024**3 - 1)
    m.read(1)
    m.close()

# Then try with two mappings
with open('test.dat', 'wb') as f:
    f.seek(8*1024**3 - 1)
    f.write(b'\0')

with open('test.dat', 'rb') as f:
    m1 = mmap.mmap(f.fileno(), 4*1024**3)
    m2 = mmap.mmap(f.fileno(), 4*1024**3, offset=4*1024**3)
    m2.read(1)
    m2.close()
    m1.close()

