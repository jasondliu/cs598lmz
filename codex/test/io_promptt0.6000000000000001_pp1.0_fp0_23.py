import io
# Test io.RawIOBase
class SubclassWithRawIO(io.RawIOBase):
    def readinto(self, buffer):
        return 0

