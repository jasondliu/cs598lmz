import io
# Test io.RawIOBase
class Stream(io.RawIOBase):
    def readinto(self, buf):
        raise NotImplementedError

stream = Stream()
