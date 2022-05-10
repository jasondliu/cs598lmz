import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(9))
    m.seek(0)
    assert list(m.read(10)) == [9] * 10

m.flush()
m.close()

with open('test', 'rb') as f:
    assert list(f.read(10)) == [9] * 10
f.close()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 2
    m.flush()

with open('test', 'rb') as f:
    assert list(f.read(10)) == [2] * 10

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:10:2] = bytes(10)
    m.flush()

with open('test', 'rb') as f:
    assert list(f.read(10)) == [0, 1] * 5

with open('test', 'r+b')
