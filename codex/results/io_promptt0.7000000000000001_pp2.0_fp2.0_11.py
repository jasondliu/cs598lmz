import io
# Test io.RawIOBase
# ------------------------------------------------------------------------------
class TestRawIOBase(unittest.TestCase):
    raw_io_base = io.RawIOBase()
    def test_constructor(self):
        "Test RawIOBase constructor"

        # No arguments
        self.assertRaises(TypeError, io.RawIOBase)

        # Wrong number of arguments
        self.assertRaises(TypeError, io.RawIOBase, 1, 2)

    def test_io_base_attributes(self):
        "Test RawIOBase attributes inherited from IOBase"

        # RawIOBase must inherit from IOBase
        self.assertTrue(issubclass(io.RawIOBase, io.IOBase))

        # Test attributes
        self.assertTrue(self.raw_io_base.readable())
        self.assertFalse(self.raw_io_base.writable())
        self.assertTrue(self.raw_io_base.seekable())

    def test_raw_io_base_methods(self):
        "Test RawIOBase methods"

        self.assertRaises(io
