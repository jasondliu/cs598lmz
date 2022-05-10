import io
# Test io.RawIOBase

class TestIO(unittest.TestCase):
    def test_RawIOBase(self):
        # Test RawIOBase's constructor
        self.assertRaises(TypeError, io.RawIOBase)

        # Test RawIOBase's attributes
        i = io.RawIOBase()
        self.assertTrue(hasattr(i, 'mode'))
        self.assertTrue(hasattr(i, 'name'))

        # Test RawIOBase's methods
        check_close = True
        try:
            i.fileno()
        except io.UnsupportedOperation:
            pass
        else:
            self.assertTrue(i.close())
            check_close = False
        self.assertTrue(hasattr(i, 'isatty'))
        self.assertTrue(i.readable())
        self.assertTrue(i.seekable())
        self.assertTrue(i.writable())
        if check_close:
            self.assertTrue(i.close())

    def test_open(self):
        # Test open()
        self.assertRaises
