import mmap
# Test mmap.mmap for the purpose of this test, any object with a
# fileno() method will do.
class MmapWrapper(io.RawIOBase):
    def __init__(self, *args):
        self.mmap = None
        self.closed = False

    def fileno(self):
        return -1

    def size(self):
        return 10

    def readinto(self, buf):
        if self.mmap is None:
            raise RuntimeError("depleted")
        assert len(buf) == len(self.mmap)
        buf[:] = self.mmap
        self.mmap = None

class TestMmapWrapper(unittest.TestCase):
    def test_mmap_is_none(self):
        m = MmapWrapper(None)
        with self.assertRaises(TypeError):
            m.readinto(bytearray(m.size()))
        self.assertTrue(m.closed)

    def test_readinto_error(self):
        m = MmapWrapper(None)
        with self.
