import mmap
# Test mmap.mmap
def test_mmap():
    m = mmap.mmap()
    m.close()

# Test mmap.mmap(size)
def test_mmap_with_size():
    m = mmap.mmap(16)
    m.close()

# Test mmap.mmap(fileno)
def test_mmap_with_fileno():
    fd = os.open('mmap.tmp', os.O_RDWR | os.O_CREAT)
    m = mmap.mmap(fd)
    m.close()
    os.close(fd)
    os.remove('mmap.tmp')

# Test mmap.mmap(fileno, size)
def test_mmap_with_fileno_size():
    fd = os.open('mmap.tmp', os.O_RDWR | os.O_CREAT)
    os.write(fd, b'X' * 16)
    m = mmap.mmap(fd, 16)
    m.close()
    os.close(fd)

