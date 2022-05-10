import mmap
# Test mmap.mmap() and mmap.write()
def test_mmap():
    s = mmap.mmap(-1, 13)
    print (s)
    s.write(b'Hello Python!')
    assert s[:] == b'Hello Python!'
# Test mmap.read()
def test_read():
    s = mmap.mmap(-1, 13)
    s.write(b'Hello Python!')
    # Read from 0
    assert s.read(5) == b'Hello'
    # Read from 6
    assert s.read(7) == b' Python'
    # Read from 0
    assert s.read(13) == b'Hello Python!'
    # EOF
    assert s.read() == b''
# Test mmap.read_byte()
def test_read_byte():
    s = mmap.mmap(-1, 13)
    s.write(b'Hello Python!')
    # Read from 0
    assert s.read_byte() == ord(b'H')
    # Read from 1
    assert s.read_byte()
