import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\x01\x02\x03')
    m.seek(0)
    assert m.read(1) == b'\x01'
    m.close()

with open('test', 'rb') as f:
    assert f.read() == b'\x01\x02\x03'
</code>

