import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read_into(self):
        self.assertRaises(TypeError, io.RawIOBase().readinto, bytearray())
        self.assertRaises(TypeError, io.RawIOBase().readinto, memoryview(b''))
        self.assertRaises(TypeError, io.RawIOBase().readinto, array.array(
            'b', b''))

    def test_read_into_non_integer(self):
        class MyRawIO(io.RawIOBase):

            def readinto(self, b):
                return super().readinto(b)
        b = bytearray(5)
        self.assertRaises(TypeError, MyRawIO().readinto, b, None)

    def test_read_into_negative_size(self):
        class MyRawIO(io.RawIOBase):

            def readinto(self, b):
                return super().readinto(b)
        b = bytearray(5)
        self.assertRaises
