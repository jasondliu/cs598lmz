import io
# Test io.RawIOBase
# io.RawIOBase.readinto()

class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        self.assertRaises(TypeError, io.RawIOBase.readinto, None)

    def test_readinto_non_integer_buffer(self):
        # Issue #16791: readinto should raise a TypeError if the buffer
        # argument is not an integer.
        class TestRawIO(io.RawIOBase):
            def readinto(self, buf):
                pass
        with self.assertRaises(TypeError):
            TestRawIO().readinto(b'')

    def test_readinto_non_writable_buffer(self):
        # Issue #16791: readinto should raise a TypeError if the buffer
        # argument is not writable.
        class TestRawIO(io.RawIOBase):
            def readinto(self, buf):
                pass
        with self.assertRaises(TypeError):
            TestRawIO().readinto(array.array('i', [1]))


