import io
class File(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.offset = 0
    def read(self, n):
        if self.offset + n > len(self.data):
            n = len(self.data) - self.offset
        chunk = self.data[self.offset:self.offset+n]
        self.offset += n
        return chunk

f = File(data)
if f.read(5) != data[:5]:
    raise AssertionError
f.seek(10)
if f.read(5) != data[10:15]:
    raise AssertionError
f.seek(10)
if f.read(25) != data[10:35]:
    raise AssertionError

class File(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.offset = 0
    def readinto(self, b):
        n = len(b)
        if self.offset + n > len(self.data):
            n = len(self.
