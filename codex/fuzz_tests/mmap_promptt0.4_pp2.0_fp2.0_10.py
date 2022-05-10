import mmap
# Test mmap.mmap(0, size, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, fd, 0)

def test_mmap(size):
    # mmap.mmap(0, size, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, fd, 0)
    fd = os.open('/dev/zero', os.O_RDWR)
    mm = mmap.mmap(fd, size)
    mm.close()

def test_mmap_alloc(size):
    # mmap.mmap(0, size, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, fd, 0)
    fd = os.open('/dev/zero', os.O_RDWR)
    mm = mmap.mmap(fd, size)
    mm.close()

def test_mmap_alloc_malloc(size):
    # mmap.mmap(0, size
