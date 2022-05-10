import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[0] = ord('x')
                return 1
        self.assertEqual(b'x', TestRawIO().read(1))
        self.assertEqual(b'x', bytearray(b' ' * 10)[0:1])
        self.assertEqual(b'x', bytearray(b' ' * 10)[0:1])
        self.assertRaises(TypeError, TestRawIO().readinto, memoryview(bytearray(b' ' * 10)))
        self.assertRaises(TypeError, TestRawIO().readinto, memoryview(bytearray(b' ' * 10)))
        self.assertRaises(TypeError, TestRawIO().readinto, memoryview(bytearray(b' ' * 10)))
        self.assertRaises(TypeError, TestRawIO().readinto, memoryview(byt
