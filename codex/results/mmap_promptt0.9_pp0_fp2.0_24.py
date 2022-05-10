import mmap
# Test mmap.mmap(MMAP_LEN).read() and mmap.SEEK_SET

MMAP_LEN = 8192

def test_func(filename):
    print("Testing mmap.mmap(%d).read() on %r:", MMAP_LEN, filename)

    m = mmap.mmap(os.open(filename, os.O_RDONLY), MMAP_LEN)
    #pos = m.tell()
    #print("Current position: %d" % pos)
    #m.seek(MMAP_LEN, os.SEEK_SET)
    #pos = m.tell()
    #print("New position: %d" % pos)
    m.seek(0, os.SEEK_SET)
    #pos = m.tell()
    #print("position after seek(0): %d" % pos)
    data = m.read(MMAP_LEN)
    m.close()
#    return len(data)
    return 0

print(test_func('mmap_read_test.py'))
