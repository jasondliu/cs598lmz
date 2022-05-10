import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        # Test readinto
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                b[:] = b'foo'
                return 3
        b = bytearray(5)
        self.assertEqual(TestRawIO().readinto(b), 3)
        self.assertEqual(b, b'foo\x00\x00')
    def test_readinto_array(self):
        # Test readinto with array.array
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                b[:] = b'foo'
                return 3
        b = array.array('b', b'00000')
        self.assertEqual(TestRawIO().readinto(b), 3)
        self.assertEqual(b, array.array('b', b'foo\x00\x
