import io
# Test io.RawIOBase class


class MyRawIO(io.RawIOBase):

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        return 0

    def write(self, b):
        return 0


class TestRawIOBase(unittest.TestCase):
    def test_new(self):
        self.assertRaises(TypeError, io.RawIOBase)

    def test_incomplete(self):
        self.assertRaises(io.BlockingIOError, MyRawIO().readinto, b'')
        self.assertRaises(io.BlockingIOError, MyRawIO().write, b'')


if __name__ == "__main__":
    unittest.main()
