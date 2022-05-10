import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                return 0
        self.assertEqual(TestRawIO().readinto(bytearray()), 0)
        self.assertRaises(TypeError, TestRawIO().readinto, None)
        self.assertRaises(TypeError, TestRawIO().readinto, "")
        self.assertRaises(TypeError, TestRawIO().readinto, u"")
        self.assertRaises(TypeError, TestRawIO().readinto, 0)
        self.assertRaises(TypeError, TestRawIO().readinto, 0.0)
        self.assertRaises(TypeError, TestRawIO().readinto, [])
        self.assertRaises(TypeError, TestRawIO().readinto, ())
        self.assertRaises(TypeError, TestRawIO().readinto, {})
        self.assertRaises(TypeError, TestRawIO().readinto, set
