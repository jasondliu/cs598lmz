import io
# Test io.RawIOBase
# Test io.BufferedIOBase
# Test io.IOBase

class TestIoObjects(unittest.TestCase):

    def test_io_buffer_io(self):
        # Test io.BufferedIOBase
        self.assertIsInstance(io.BufferedIOBase, type)
        self.assertTrue(issubclass(io.BufferedIOBase, io.IOBase))

    def test_io_file_io(self):
        # Test io.RawIOBase
        self.assertIsInstance(io.RawIOBase, type)
        self.assertTrue(issubclass(io.RawIOBase, io.IOBase))
        s = io.StringIO("HelloWorld")
        self.assertTrue(isinstance(s, io.BufferedIOBase))
        self.assertTrue(isinstance(s, io.TextIOBase))

    def test_io_base(self):
        self.assertIsInstance(io.IOBase, type)
        self.assertTrue(issubclass(io.TextIOBase, io.IOBase))
        self
