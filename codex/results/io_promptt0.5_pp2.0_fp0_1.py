import io
# Test io.RawIOBase

class RawIOTest(unittest.TestCase):
    def test_attributes(self):
        self.assertIsInstance(io.RawIOBase.read, collections.abc.Callable)
        self.assertIsInstance(io.RawIOBase.read1, collections.abc.Callable)
        self.assertIsInstance(io.RawIOBase.write, collections.abc.Callable)
        self.assertIsInstance(io.RawIOBase.fileno, collections.abc.Callable)
        self.assertIsInstance(io.RawIOBase.seekable, collections.abc.Callable)
        self.assertIsInstance(io.RawIOBase.readable, collections.abc.Callable)
        self.assertIsInstance(io.RawIOBase.writable, collections.abc.Callable)
        self.assertIsInstance(io.RawIOBase.seek, collections.abc.Callable)
        self.assertIsInstance(io.RawIOBase.tell, collections.abc.Callable)
        self.assertIsInstance(io.RawIOBase.truncate, collections
