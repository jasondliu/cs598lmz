import io
# Test io.RawIOBase.readinto()

class TestRawIOBaseReadinto(unittest.TestCase):

    def test_readinto(self):
        # readinto() should return an integer.
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                return len(b)
        self.assertEqual(TestRawIO().readinto(bytearray(10)), 10)

        # readinto() should accept any object that implements the buffer API.
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                return len(b)
        self.assertEqual(TestRawIO().readinto(memoryview(bytearray(10))), 10)

        # readinto() should raise io.UnsupportedOperation if not overridden.
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytearray(10))

    def test_readinto_after_close(self):
        # Issue #14056: readinto() should raise ValueError after the file

