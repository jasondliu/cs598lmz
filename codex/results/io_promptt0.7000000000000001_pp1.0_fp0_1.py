import io
# Test io.RawIOBase.write()

# Set up buffers.
import array
buffer = array.array('c', ' '*4096)
buffer2 = array.array('c', ' '*4096)

# Check that RawIOBase.write() writes the right amount.
class TestRawIO(io.RawIOBase):
    def write(self, b):
        n = len(b)
        # Check that the write() method returns the correct value.
        r = io.RawIOBase.write(self, b)
        assert r == n
        # Check that the bytes have been written to the internal buffer.
        assert buffer[:n] == array.array('c', b)
        # Check that the bytes have not been written past the internal buffer.
        assert buffer[n] == ' '
        return r
test = TestRawIO()
test.write(buffer2)

# Check that RawIOBase.write() returns the right value.
assert test.write(buffer2) == len(buffer2)
