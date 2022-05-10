import io
# Test io.RawIOBase

class RawIOBaseTest(unittest.TestCase):
    def test_args(self):
        # IOError is raised when args are wrong
        self.assertRaises(TypeError, io.RawIOBase)
        self.assertRaises(TypeError, io.RawIOBase, "foo")
        self.assertRaises(TypeError, io.RawIOBase, None, None)
        self.assertRaises(TypeError, io.RawIOBase, UnseekableIO(""))
        self.assertRaises(TypeError, io.RawIOBase, UnseekableIO(""), None)
        self.assertRaises(TypeError, io.RawIOBase, None, "foo")
        self.assertRaises(ValueError, io.RawIOBase, UnseekableIO(""), -1)

    def test_read(self):
        # IOError is raised when the underlying raw stream has problems
        self.assertRaises(IOError, io.RawIOBase(UnreadableRawIO()).read)
        self.assertRaises(IOError, io.RawIOBase(Un
