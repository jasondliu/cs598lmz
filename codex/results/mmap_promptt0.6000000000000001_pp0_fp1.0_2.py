import mmap
# Test mmap.mmap()
def test_mmap(filename, size):
    f = os.open(filename, os.O_RDWR | os.O_CREAT, 0666)
    os.write(f, '\x00' * size)
    m = mmap.mmap(f, size)
    m[0] = '3'
    m.close()
    os.close(f)
    return
test_mmap('/tmp/test.txt', 10)

# Test mmap.mmap(fileno, length, flags, prot, access, offset, fileno, closefd)
def test_mmap2(filename, size):
    f = os.open(filename, os.O_RDWR | os.O_CREAT, 0666)
    os.write(f, '\x00' * size)
    m = mmap.mmap(f, size, access=mmap.ACCESS_WRITE)
    m[0] = '3'
    m.close()
    os.close(f)
    return
test_mmap2('/
