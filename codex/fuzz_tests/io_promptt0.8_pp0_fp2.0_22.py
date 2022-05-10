import io
# Test io.RawIOBase() with readinto()

class TestRawIOBaseReadInto(unittest.TestCase):

    def test_readinto1(self):
        # Test readinto() as implemented in io.BufferedIOBase
        t = io.BytesIO(b"XXX")
        b = bytearray(2)
        self.assertEqual(t.readinto1(b), len(b))
        self.assertEqual(t.tell(), len(b))
        self.assertEqual(t.readinto1(b), 1)
        self.assertEqual(t.tell(), 3)
        self.assertEqual(t.readinto1(b), 0)
        self.assertEqual(t.tell(), 3)
        self.assertEqual(b[:3], b"XXY")

    def test_readinto(self):
        # Test readinto() as implemented in io.RawIOBase
        t = io.BytesIO(b"XXX")
        b = bytearray(2)
        self.assertEqual(t.readinto(b
