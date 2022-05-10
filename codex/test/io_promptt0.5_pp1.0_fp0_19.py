import io
# Test io.RawIOBase
class RawIOBaseSubclass(io.RawIOBase):
    def __init__(self, value):
        self.value = value
    def read(self, n=-1):
        return self.value
    def write(self, b):
        self.value = b
    def close(self):
        pass

