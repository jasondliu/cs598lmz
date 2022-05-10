import io
# Test io.RawIOBase subclass that reads only one character.
# This is a base class; you have to implement readinto() yourself.

class OneByteIO(io.RawIOBase):
    def __init__(self, byte):
        self.byte = byte

    def readable(self):
        return True

    def readinto(self, buf):
        buf[0] = self.byte
        return 1

    def readall(self):
        return self.byte

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        if whence != io.SEEK_SET:
            raise IOError("can't do non-zero cur-relative seeks")
        if offset != 0:
            raise IOError("can only seek to beginning")
        return 0

    def tell(self):
        return 0

# Test io.BytesIO, a buffered I/O implementation using an in-memory bytes
# buffer.  The initial_bytes argument lets you specify a bytes object with
# initial contents.

class BytesIOTest(unittest.Test
