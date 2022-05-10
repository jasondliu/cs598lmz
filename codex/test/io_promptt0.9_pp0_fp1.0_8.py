import io
# Test io.RawIOBase
class RawI(io.RawIOBase):
    def readinto(self, b):
        pass
    def writable(self):
        return True
    def write(self, b):
        pass

