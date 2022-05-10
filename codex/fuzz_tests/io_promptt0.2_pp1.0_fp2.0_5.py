import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:3] = b'foo'
                return 3
        buf = bytearray(5)
        f = TestRawIO()
        n = f.readinto(buf)
        self.assertEqual(n, 3)
        self.assertEqual(buf, b'foo\x00\x00')
        self.assertEqual(f.readinto(buf), 0)
        self.assertEqual(buf, b'foo\x00\x00')
        buf = bytearray(2)
        self.assertRaises(TypeError, f.readinto, buf, 5)
        self.assertRaises(TypeError, f.readinto, memoryview(buf))
        self.assertRaises(TypeError, f.readinto, 'foo')
        self.assertRaises(TypeError, f.readinto, bytearray(b
