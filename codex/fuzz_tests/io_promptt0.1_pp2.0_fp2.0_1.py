import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b"xy"
        self.assertEqual(TestRawIO().read(), b"xy")
        self.assertEqual(TestRawIO().read(None), b"xy")
        self.assertEqual(TestRawIO().read(0), b"")
        self.assertEqual(TestRawIO().read(-1), b"xy")
        self.assertEqual(TestRawIO().read(1), b"x")
        self.assertEqual(TestRawIO().read(2), b"xy")
        self.assertEqual(TestRawIO().read(3), b"xy")
        self.assertEqual(TestRawIO().read(sys.maxsize), b"xy")
        self.assertRaises(TypeError, TestRawIO().read, "")
        self.assertRaises(TypeError, Test
