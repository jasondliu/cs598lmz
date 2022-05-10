import io
# Test io.RawIOBase
class test_RawIOBase(unittest.TestCase):
    def test_readinto(self):
        # Issue #7995: RawIOBase.readinto() should return None
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                self.readinto_called = True
                return 0
        r = MyRawIO()
        self.assertEqual(r.readinto(b''), None)
        self.assertTrue(r.readinto_called)
    def test_readinto_negative_arg(self):
        # Issue #18018: readinto() should raise ValueError if given a negative
        # argument.
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                self.readinto_called = True
                return 0
        r = MyRawIO()
        self.assertRaises(ValueError, r.readinto, bytearray(-1))
        self.assertFalse(hasattr(r, 'readinto_called'))
    def test_readinto_resize
