import io
# Test io.RawIOBase

class TestRawIOBase(unittest.TestCase):

    def test_readinto(self):
        # Test readinto()
        b = bytearray(b"abc")
        self.assertEqual(io.BytesIO(b"xyz").readinto(b), 3)
        self.assertEqual(b, b"xyz")
        self.assertRaises(TypeError, io.BytesIO(b"xyz").readinto, memoryview(b))
        self.assertRaises(TypeError, io.BytesIO(b"xyz").readinto, "abc")
        self.assertRaises(TypeError, io.BytesIO(b"xyz").readinto, u"abc")

    def test_readall(self):
        # Test readall()
        self.assertEqual(io.BytesIO(b"xyz").readall(), b"xyz")
        self.assertEqual(io.BytesIO(b"xyz").readall(), b"")

    def test_read(self):
        # Test read()
        self.
