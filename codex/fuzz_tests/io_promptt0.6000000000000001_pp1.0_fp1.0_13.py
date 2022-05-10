import io
# Test io.RawIOBase

class RawIOTest(unittest.TestCase):

    def test_constructor(self):
        self.assertRaises(TypeError, io.RawIOBase)

    def test_abc(self):
        self.assertTrue(issubclass(io.RawIOBase, io.IOBase),
                        "RawIOBase is not a subclass of IOBase")
        self.assertTrue(issubclass(io.RawIOBase, io.RawIOBase),
                        "RawIOBase is not a subclass of RawIOBase")
        self.assertFalse(issubclass(io.RawIOBase, io.BufferedIOBase),
                         "RawIOBase is a subclass of BufferedIOBase")
        self.assertFalse(issubclass(io.RawIOBase, io.TextIOBase),
                         "RawIOBase is a subclass of TextIOBase")

        for attr in ('read', 'readinto', 'write', 'fileno', 'seek', 'tell',
                     'truncate', 'close', 'readable', 'writable', 'seekable',
                     'isatty
