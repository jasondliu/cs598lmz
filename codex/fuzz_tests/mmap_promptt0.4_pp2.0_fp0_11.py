import mmap
# Test mmap.mmap.resize

with open('testfile', 'wb') as f:
    f.write(b'\x00' * 100)

m = mmap.mmap(f.fileno(), 0)
m.resize(50)
assert len(m) == 50

m.resize(150)
assert len(m) == 150
m[:] = b'\x01' * 150

with open('testfile', 'rb') as f:
    assert f.read() == b'\x01' * 150

m.close()
