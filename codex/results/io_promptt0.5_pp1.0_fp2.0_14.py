import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):

    def test_readinto(self):
        # Test that readinto() returns None, and doesn't raise an
        # exception.
        self.assertIsNone(io.RawIOBase().readinto(bytearray()))
        self.assertIsNone(io.RawIOBase().readinto(memoryview(b'')))


if __name__ == '__main__':
    unittest.main()
