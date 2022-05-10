import io
# Test io.RawIOBase

class TestRawIOBase(unittest.TestCase):
    def test_ctor(self):
        self.assertRaises(TypeError, io.RawIOBase)
        self.assertRaises(TypeError, io.RawIOBase, 'spam')

    def test_error_properties(self):
        raw = io.RawIOBase()
        self.assertEqual(raw.errno, 0)
        self.assertEqual(raw.strerror, '')

    def test_filename_property(self):
        raw = io.RawIOBase()
        self.assertEqual(raw.name, None)

    def test_readinto(self):
        raw = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation,
                          raw.readinto, bytearray())

    def test_read(self):
        raw = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, raw.read)

    def test_readall(self):
        raw = io.RawIOBase()
       
