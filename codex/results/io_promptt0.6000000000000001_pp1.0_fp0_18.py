import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        f = io.RawIOBase()
        self.assertRaises(NotImplementedError, f.readinto, None)

    def test_readinto_array(self):
        f = io.RawIOBase()
        a = array.array('i', [0])
        self.assertRaises(NotImplementedError, f.readinto, a)

    def test_readinto_bytearray(self):
        f = io.RawIOBase()
        b = bytearray(1)
        self.assertRaises(NotImplementedError, f.readinto, b)

    def test_readinto_memoryview(self):
        f = io.RawIOBase()
        m = memoryview(bytearray(1))
        self.assertRaises(NotImplementedError, f.readinto, m)

    def test_readinto_buffer(self):
        f = io.RawIOBase()
        b = buffer(by
