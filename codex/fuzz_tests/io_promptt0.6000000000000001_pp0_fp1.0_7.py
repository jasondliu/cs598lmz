import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_init(self):
        # io.RawIOBase()
        with self.assertRaises(TypeError):
            io.RawIOBase()
    def test_read(self):
        # io.RawIOBase.read()
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase.read(None)
    def test_readinto(self):
        # io.RawIOBase.readinto()
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase.readinto(None)
    def test_write(self):
        # io.RawIOBase.write()
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase.write(None)

# Test io.RawIOBase.read()
class RawIOBaseReadTest(unittest.TestCase):
    def test_read_positional(self):
        # io.RawIOBase.read()
        class TestRawIO(io.
