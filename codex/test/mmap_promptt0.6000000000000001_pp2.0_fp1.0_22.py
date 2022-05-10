import mmap
# Test mmap.mmap()

def test_mmap(filename):
    fd = os.open(filename, os.O_RDWR)
    m = mmap.mmap(fd, 0)
    m.write(b'abcd')
    m.flush()
    m.close()
    os.close(fd)

filename = 'hello.txt'
test_mmap(filename)

# Test mmap.mmap() with a specific size

def test_mmap_with_size(filename):
    fd = os.open(filename, os.O_RDWR)
    m = mmap.mmap(fd, 4)
    m.write(b'abcd')
    m.flush()
    m.close()
    os.close(fd)

filename = 'hello.txt'
test_mmap_with_size(filename)

# Test mmap.mmap() with access=mmap.ACCESS_READ

