import mmap
# Test mmap.mmap.read()

def test_read():
    f = open('/etc/passwd', 'r')
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    assert m.read(1) == '#'
    assert m.read(5) == 'root:'
    assert m.read(1) == 'x'
    assert m.read(4) == ':0:0'
    assert m.read(1) == ':'
    m.close()
    f.close()

# Test mmap.mmap.read_byte()

def test_read_byte():
    f = open('/etc/passwd', 'r')
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    assert m.read_byte() == '#'
    assert m.read_byte() == 'r'
    assert m.read_byte() == 'o'
    assert m.read_byte() == 'o'
    assert m.read_
