import io
# Test io.RawIOBase

# io.RawIOBase.readinto()

class TestRawIOBaseReadinto(BaseTestIOBase):

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readinto, bytearray(1))

    def test_readinto_array(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readinto, array.array('b', b'x'))

    def test_readinto_memoryview(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readinto, memoryview(b'x'))

    def test_readinto_bytearray(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readinto, bytearray(b'x'))

    def test_readinto_readonly_buffer(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readinto, buffer(b'x'))

    def test_readinto_readonly_array(self):
