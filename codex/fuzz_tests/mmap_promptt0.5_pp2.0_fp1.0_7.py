import mmap
# Test mmap.mmap

def test_mmap_mmap():
    # Test mmap.mmap
    f = open('/dev/zero')
    m = mmap.mmap(f.fileno(), 0)
    m.close()
    f.close()

def test_mmap_mmap_copy():
    # Test mmap.mmap
    f = open('/dev/zero')
    m = mmap.mmap(f.fileno(), 0)
    m2 = m.copy()
    m2.close()
    m.close()
    f.close()

def test_mmap_mmap_read():
    # Test mmap.mmap
    f = open('/dev/zero')
    m = mmap.mmap(f.fileno(), 0)
    m.read(1)
    m.close()
    f.close()

def test_mmap_mmap_write():
    # Test mmap.mmap
    f = open('/dev/zero')
    m = mmap.mmap(f.fileno
