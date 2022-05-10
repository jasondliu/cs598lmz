import io
# Test io.RawIOBase.readinto()

class TestRawIO(io.RawIOBase):
    def __init__(self, source):
        self.source = source
    def readinto(self, b):
        s = self.source.read(len(b))
        n = len(s)
        try:
            b[:n] = s
        except TypeError as err:
            # If the buffer is not writeable, a TypeError should be raised.
            if 'read-only' in str(err):
                return n
            # Otherwise, this is some other kind of TypeError, so re-raise it.
            raise
        return n
    def readable(self):
        return True

def test_readinto():
    # This function tests the operation of RawIOBase.readinto() with
    # a range of buffer types.
    for b in (bytearray(1), memoryview(bytearray(1)), array.array('b', b' ')):
        # Test reading into a non-empty buffer
        b[:] = b'x'
        r = Test
