import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b"xyzzy"
        self.assertEqual(TestRawIO().read(), b"xyzzy")
        self.assertEqual(TestRawIO().read(None), b"xyzzy")
        self.assertEqual(TestRawIO().read(0), b"")
        self.assertEqual(TestRawIO().read(2), b"xy")
        self.assertEqual(TestRawIO().read(-1), b"xyzzy")
        self.assertEqual(TestRawIO().read(-2), b"xyzzy")
        self.assertEqual(TestRawIO().read(-3), b"xyzzy")
        self.assertEqual(TestRawIO().read(-4), b"xyzzy")
        self.assertEqual(TestRawIO().read(-100), b"xyzzy")
        self.assertE
