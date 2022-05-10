import mmap
# Test mmap.mmap()
with open('/tmp/mapped.file', 'w+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'0123456789abcdef')
    m.seek(0)
    print(m.read(4))
    print(m.read(4))
    m.seek(0)
    print(m.read(4))
    m.seek(10)
    print(m.read(1))
    m.close()
# Test mmap.mmap() with offset
with open('/tmp/mapped.file', 'w+b') as f:
    m = mmap.mmap(f.fileno(), 16, offset=1)
    m.write(b'abcdefghijklmnopqrstuvwxyz')
    m.seek(0)
    print(m.read(4))
    m.seek(0)
    print(m[:4])
    m.close()
# Test mmap.mmap() with offset
with open('
