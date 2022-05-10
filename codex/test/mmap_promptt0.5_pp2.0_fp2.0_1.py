import mmap
# Test mmap.mmap.read()

with open('test_mmap.txt', 'w') as f:
    f.write('0123456789')

with open('test_mmap.txt', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.read(5)
    m.read(1)
    m.read(1)
    m.read(1)
    m.read(1)
    m.read(1)

