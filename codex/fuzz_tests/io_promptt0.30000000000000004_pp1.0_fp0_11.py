import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b'x' * n
        self.assertEqual(TestRawIO().read(), b'x')
        self.assertEqual(TestRawIO().read(0), b'')
        self.assertEqual(TestRawIO().read(10), b'x' * 10)
        self.assertEqual(TestRawIO().read(-1), b'x')
        self.assertEqual(TestRawIO().read(-2), b'x')
        self.assertEqual(TestRawIO().read(-3), b'x')
        self.assertEqual(TestRawIO().read(sys.maxsize), b'x' * sys.maxsize)
        self.assertEqual(TestRawIO().read(sys.maxsize + 1), b'x' * (sys.maxsize + 1))
        self.assertE
