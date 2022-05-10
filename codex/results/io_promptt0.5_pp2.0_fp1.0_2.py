import io
# Test io.RawIOBase
# Test io.BufferedIOBase
# Test io.IOBase

class IOBaseTests(unittest.TestCase):

    def test_attributes(self):
        self.assertEqual(io.BlockingIOError.characters_written, None)
        self.assertEqual(io.BlockingIOError.errno, None)
        self.assertEqual(io.BlockingIOError.filename, None)
        self.assertEqual(io.BlockingIOError.strerror, None)

    def test_io_base(self):
        self.assertRaises(TypeError, io.IOBase)

        class MyIO(io.IOBase):
            pass

        self.assertRaises(TypeError, MyIO)

    def test_read_into(self):
        class MyIO(io.IOBase):
            def read(self, n=-1):
                return b'x'*n

        b = bytearray(10)
        self.assertEqual(MyIO().readinto(b), 10)
        self.assert
