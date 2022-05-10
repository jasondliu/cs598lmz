import io
# Test io.RawIOBase.readinto()

class TestRawIOBaseReadinto(unittest.TestCase):
    def test_readinto(self):
        # Read bytes into a bytearray
        b = bytearray(b'\0'*10)
        n = io.BytesIO(b"abcdef").readinto(b)
        self.assertEqual(n, 6)
        self.assertEqual(b[:6], b"abcdef")
        self.assertEqual(b[6:], b'\0'*4)
        # Read bytes into a memoryview
        b = bytearray(b'\0'*10)
        m = memoryview(b)
        n = io.BytesIO(b"abcdef").readinto(m)
        self.assertEqual(n, 6)
        self.assertEqual(b[:6], b"abcdef")
        self.assertEqual(b[6:], b'\0'*4)
        # Read bytes into an array
        b = array.array('b', b'\
