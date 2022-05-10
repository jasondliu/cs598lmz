import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        # Test a readinto implementation.
        class MockRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:] = b'\x01\x02\x03\x04'
                return len(b)

        b = bytearray(4)
        r = MockRawIO()
        n = r.readinto(b)
        self.assertEqual(n, 4)
        self.assertEqual(b, b'\x01\x02\x03\x04')

        # Test that readinto() doesn't accept keyword arguments
        self.assertRaises(TypeError, r.readinto, memoryview(b), foo=42)

    def test_readinto_resize(self):
        # Test a readinto implementation that resizes the buffer.
        class MockRawIO(io.RawIOBase):
            def readinto(self, b):
                del b[:]
                b.extend(b'\
