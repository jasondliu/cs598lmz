import mmap
# Test mmap.mmap
try:
    # Python 2.x
    import StringIO
    StringIO = StringIO.StringIO
except ImportError:
    # Python 3.x
    from io import BytesIO as StringIO

def test_mmap_empty_file():
    # Reduce the size of the original file, just to be sure
    filename = basename + ".mmap.tst"
    create_file_of_size(filename, 0)
    f = open(filename, "rb+")
    m = mmap.mmap(f.fileno(), 0, close=True)
    assert m.size() == 0, "empty mmap must have 0 size"
    assert len(m) == 0, "empty bytes of empty mmap must have 0 length"
    f.close()
    os.unlink(filename)

def test_mmap_file():
    filename = basename + ".mmap.tst"
    size = testsize - 1
    create_file_of_size(filename, size + 1)
    f = open(filename, "rb+")
    m
