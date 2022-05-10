import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
    def test_readinto(self):
        # Test that readinto() returns the number of bytes read.
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                return 0
        self.assertEqual(TestRawIO().readinto(bytearray()), 0)
        self.assertEqual(TestRawIO().readinto(memoryview(bytearray())), 0)
        self.assertEqual(TestRawIO().readinto(memoryview(bytearray(1))), 0)
        self.assertEqual(TestRawIO().readinto(bytearray(1)), 0)
        self.assertEqual(TestRawIO().readinto(bytearray(5)), 0)
        self.assertEqual(TestRawIO().readinto(bytearray(100)), 0)
        self.assertEqual(TestRawIO().readinto(bytearray(1000000)), 0)
        class TestRawIO(io.RawIOBase):
           
