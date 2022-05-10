import io
# Test io.RawIOBase

class TestRawIOBase(unittest.TestCase):

    def test_constructor(self):
        self.assertRaises(TypeError, io.RawIOBase)

    def test_read(self):
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                self.readinto_calls += 1
                return 0
        rawio = TestRawIO()
        rawio.readinto_calls = 0
        self.assertEqual(rawio.read(), b'')
        self.assertEqual(rawio.readinto_calls, 1)
        self.assertEqual(rawio.read(10), b'')
        self.assertEqual(rawio.readinto_calls, 2)
        self.assertEqual(rawio.readinto(bytearray(10)), 0)
        self.assertEqual(rawio.readinto_calls, 3)

    def test_read_non_integer(self):
        class TestRawIO(
