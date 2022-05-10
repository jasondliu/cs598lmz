import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
    def test_readinto(self):
        # Test RawIOBase.readinto()
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:] = b'\x01\x02\x03\x04'
                return len(b)
        b = bytearray(2)
        self.assertEqual(TestRawIO().readinto(b), 2)
        self.assertEqual(bytes(b), b'\x01\x02')
        self.assertRaises(TypeError, TestRawIO().readinto, memoryview(b'abcde'))

    def test_readinto_resize(self):
        # Test RawIOBase.readinto() with resizing
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:] = b'\x01\x02\x03\x04'
                return len(b)
        b = bytearray(2)
       
