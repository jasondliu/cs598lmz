import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_readinto(self):
        # Test that RawIOBase.readinto() is implemented and working.
        # readinto() should work even if read() is absent or broken.
        class ReadintoOnly(io.RawIOBase):
            def readinto(self, b):
                return len(b)
        b = bytearray(10)
        self.assertEqual(ReadintoOnly().readinto(b), 10)
        self.assertEqual(ReadintoOnly().readinto(b), 10)
        self.assertEqual(ReadintoOnly().readinto(b), 10)
        self.assertEqual(ReadintoOnly().readinto(b), 10)
        self.assertEqual(ReadintoOnly().readinto(b), 10)

    def test_readinto_error(self):
        class ReadintoOnly(io.RawIOBase):
            def readinto(self, b):
                raise OSError()

        with self.assertRaises(OSError):
            ReadintoOnly().
