import io
# Test io.RawIOBase
class IOBaseTest(unittest.TestCase):
    def test_readinto(self):
        # Issue #12359: calling RawIOBase.readinto() with a non-integer
        # object for the size argument should raise a TypeError.
        class TestRawIO(io.RawIOBase):
            def readinto(self, buf):
                return 0
        self.assertRaises(TypeError, TestRawIO().readinto, bytearray(b''),
            'not an integer')
    def test_repr(self):
        self.assertRegex(repr(io.IOBase()), '^<io.IOBase>$')
        class TestIO(io.IOBase):
            pass
        self.assertRegex(repr(TestIO()), '^<unittest.mock.Mock object at 0x[0-9a-f]+>$')
        class TestRawIO(io.RawIOBase):
            pass
        self.assertRegex(repr(TestRawIO()), '^<unittest.mock.M
