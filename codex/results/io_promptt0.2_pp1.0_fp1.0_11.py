import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b"xyz"
        self.assertEqual(TestRawIO().read(), b"xyz")
        self.assertEqual(TestRawIO().read(None), b"xyz")
        self.assertEqual(TestRawIO().read(2), b"xy")
        self.assertEqual(TestRawIO().read(-1), b"xyz")
        self.assertEqual(TestRawIO().read(0), b"")
        self.assertEqual(TestRawIO().read(42), b"xyz")
        self.assertRaises(TypeError, TestRawIO().read, "foo")
        self.assertRaises(TypeError, TestRawIO().read, b"foo")
        self.assertRaises(TypeError, TestRawIO().read, bytearray(b"foo"))
       
