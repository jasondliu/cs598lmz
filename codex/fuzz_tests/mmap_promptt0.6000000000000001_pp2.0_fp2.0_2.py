import mmap
# Test mmap.mmap(0, length[, access[, flags]])

length = 100

# read-only open
with open('mmap_test.txt', 'r+b') as f:
    m = mmap.mmap(f.fileno(), length)
    s = m.read(length)
    if s != b'abcdefghijklmnopqrstuvwxyz':
        print(repr(s))
    m.seek(0)
    m.write(b'AB')
    m.seek(len(s) - 1)
    m.write(b'Z')
    m.flush()
    m.close()
    f.seek(0)
    s = f.read(length)
    if s != b'ABcdefghijklmnopqrstuvwxyZ':
        print(repr(s))
    f.close()

# read-write open
with open('mmap_test.txt', 'r+b') as f:
    m = mmap.mmap(f.fileno(), length)
   
