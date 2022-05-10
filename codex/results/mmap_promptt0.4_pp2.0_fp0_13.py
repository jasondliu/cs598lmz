import mmap
# Test mmap.mmap.write_byte

with open('testfile', 'wb') as f:
    f.write(b'\x00' * 10)

with open('testfile', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write_byte(b'1')
    m.seek(0)
    assert m.read(1) == b'1'
    assert m.read(1) == b'\x00'

with open('testfile', 'rb') as f:
    assert f.read() == b'1\x00\x00\x00\x00\x00\x00\x00\x00\x00'

os.unlink('testfile')
