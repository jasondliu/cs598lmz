import io
# Test io.RawIOBase for readinto()
class FileIO(io.RawIOBase):

    def readinto(self, b):
        b[:] = b"\x00\x01\x02\x03"
        return len(b)

    def readable(self):
        return True

# Test io.IOBase for readinto()
class FileLike(io.IOBase):

    def readinto(self, b):
        b[:] = b"\x00\x01\x02\x03"
        return len(b)

    def readable(self):
        return True

