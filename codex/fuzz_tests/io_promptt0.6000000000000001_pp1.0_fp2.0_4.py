import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):

    def test_readinto_negative(self):
        # Issue #14056: a negative argument to RawIOBase.readinto()
        # should raise ValueError.
        r = io.RawIOBase()
        self.assertRaises(ValueError, r.readinto, bytearray(-1))

    def test_readinto_zero(self):
        # Issue #14056: a zero argument to RawIOBase.readinto()
        # should raise ValueError.
        r = io.RawIOBase()
        self.assertRaises(ValueError, r.readinto, bytearray(0))

    def test_readinto_none(self):
        # Issue #14056: a None argument to RawIOBase.readinto()
        # should raise TypeError.
        r = io.RawIOBase()
        self.assertRaises(TypeError, r.readinto, None)

    def test_readinto_bytes(self):
        # Issue #14056: a bytes argument to RawIO
