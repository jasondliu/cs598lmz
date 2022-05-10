import mmap
# Test mmap.mmap mapping at offsets other than page-alignment.
class TestMmapMapping(object):
    def test_mmap_mapping(self):
        f = open(fnm, "rb+")
        f.write(b"aaaaaaaaa")
        f.flush()
        m = mmap.mmap(f.fileno(), 10, access=mmap.ACCESS_WRITE)
        m.flush()

    def test_mmap_mapping_unreadable(self):
        fd = os.open(fnm, os.O_RDWR | os.O_CREAT)
        f = open(fnm, "rb+")
        try:
            m = mmap.mmap(f.fileno(), 10)
        except OSError:
            pass
        else:
            raise self.failureException("Expected OSError.")
        f.close()
        f = open(fnm, "rb+")
        m = mmap.mmap(f.fileno(), 10, access=mmap.ACCESS_WRITE)
        m
