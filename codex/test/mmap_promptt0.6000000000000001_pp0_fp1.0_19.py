import mmap
# Test mmap.mmap(2)
def test_mmap_mmap_2():
    print("Testing mmap.mmap(2)")
    f = open("/dev/zero")
    m = mmap.mmap(f.fileno(), 0)
    m.close()
    f.close()

# Test mmap.mmap(3)
def test_mmap_mmap_3():
    print("Testing mmap.mmap(3)")
    f = open("/dev/zero")
    m = mmap.mmap(f.fileno(), 0, mmap.MAP_SHARED)
    m.close()
    f.close()

# Test mmap.mmap(4)
def test_mmap_mmap_4():
    print("Testing mmap.mmap(4)")
    f = open("/dev/zero")
    m = mmap.mmap(f.fileno(), 0, mmap.MAP_PRIVATE, mmap.PROT_READ)
    m.close()
    f.close()

# Test
