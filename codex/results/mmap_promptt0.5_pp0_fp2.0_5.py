import mmap
# Test mmap.mmap.__new__ with offset=0 and length=0
with open('/dev/zero', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.seek(0)
    m.write(b'abcdef')
    m.seek(0)
    m.write(b'123456')
    m.seek(0)
    m.write(b'ABCDEF')
    m.seek(0)
    print(m.read(6))
    m.close()

# Test mmap.mmap.__new__ with offset=0 and length=0
with open('/dev/zero', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.seek(0)
    m.write(b'abcdef')
    m.seek(0)
    m.write(b'123456')
    m.seek(0)
    m.write
