import io
# Test io.RawIOBase.
class TestRawIOBase(unittest.TestCase):
    def test_error_conditions(self):
        self.assertRaises(TypeError, io.RawIOBase)
        self.assertRaises(TypeError, io.RawIOBase.read)
        self.assertRaises(TypeError, io.RawIOBase.readinto)
        self.assertRaises(TypeError, io.RawIOBase.write)
        self.assertRaises(TypeError, io.RawIOBase.fileno)
        self.assertRaises(TypeError, io.RawIOBase.isatty)
        self.assertRaises(TypeError, io.RawIOBase.flush)
        self.assertRaises(TypeError, io.RawIOBase.close)
        self.assertRaises(TypeError, io.RawIOBase.seek)
        self.assertRaises(TypeError, io.RawIOBase.tell)
        self.assertRaises(TypeError, io.RawIOBase.truncate)
        self.assertRaises(TypeError, io.RawIO
