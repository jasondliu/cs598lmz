import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        # Test that readinto() returns the number of bytes read
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                return len(b)
        b = bytearray(10)
        self.assertEqual(MyRawIO().readinto(b), len(b))

    def test_readinto_resize(self):
        # Test that readinto() resizes the buffer
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                b.append(1)
                return 1
        b = bytearray()
        self.assertEqual(MyRawIO().readinto(b), 1)
        self.assertEqual(len(b), 1)

    def test_readinto_error(self):
        # Test that readinto() raises an error if the buffer is too small
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):

