import io
# Test io.RawIOBase.readinto()

class TestRawIOBaseReadinto(unittest.TestCase):

    def test_readinto_returns_type(self):
        # Read from an empty io.BytesIO object.
        s = io.BytesIO()
        b = bytearray(5)
        self.assertIsInstance(s.readinto(b), int)

    def test_readinto(self):
        # Read from an empty io.BytesIO object.
        s = io.BytesIO()
        b = bytearray(5)
        self.assertEqual(s.readinto(b), 0)
        self.assertEqual(b, bytearray(5))

        # Read into a bytearray object.
        s = io.BytesIO(b'Hello World')
        b = bytearray(5)
        self.assertEqual(s.readinto(b), 5)
        self.assertEqual(b, b'Hello')
        self.assertEqual(s.tell(), 5)

        # Read into an array object.

