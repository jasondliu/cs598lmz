import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_read(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().read()

    def test_readinto(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().readinto(bytearray())

    def test_readinto_buffer(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().readinto(memoryview(bytearray(10)))

    def test_read1(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().read1()

    def test_readinto1(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().readinto1(bytearray())

    def test_readinto1_buffer(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().readinto1
