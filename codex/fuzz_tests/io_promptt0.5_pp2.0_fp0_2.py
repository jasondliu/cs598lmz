import io
# Test io.RawIOBase.readinto()

class TestRawIOBaseReadinto(unittest.TestCase):

    def test_readinto_empty(self):
        # Issue #7994: readinto() on an empty RawIOBase object should return 0.
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, buf):
                return 0
        buf = bytearray(10)
        self.assertEqual(TestRawIO().readinto(buf), 0)

    def test_readinto_non_empty(self):
        # Issue #7994: readinto() on a non-empty RawIOBase object should return
        # the number of bytes read.
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, buf):
                buf[:5] = b'12345'
                return 5
        buf = bytearray(10)
        self.assertEqual(TestRawIO().readinto(buf), 5)
        self.assertE
