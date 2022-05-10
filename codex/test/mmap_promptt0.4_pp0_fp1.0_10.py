import mmap
# Test mmap.mmap.resize

with open('/tmp/test', 'w+b') as f:
    f.write(b'\0' * 100)

with mmap.mmap(f.fileno(), 0) as m:
    m.resize(200)
    m.seek(100)
    m.write(b'x' * 100)
    m.seek(0)
    assert m.read(100) == b'\0' * 100
    assert m.read(100) == b'x' * 100

