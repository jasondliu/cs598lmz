import mmap
# Test mmap.mmap(0,1) and mmap.resize()
def test_mmap_resize():
    fd = os.open('@test', os.O_RDWR | os.O_CREAT)
    os.write(fd, '\0'*10)
    os.close(fd)
    m = mmap.mmap(fd, 10)
    m.resize(20)
    m.close()
    os.unlink('@test')

# Test mmap.write() and read()
def test_mmap_write_read():
    fd = os.open('@test', os.O_RDWR | os.O_CREAT)
    os.write(fd, '\0'*10)
    os.close(fd)
    m = mmap.mmap(fd, 10)
    m.write('abcd')
    m.seek(0)
    assert m.read(4) == 'abcd'
    m.close()
    os.unlink('@test')

# Test mmap.move()
def test
