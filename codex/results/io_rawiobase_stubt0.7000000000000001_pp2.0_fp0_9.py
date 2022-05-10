import io
class File(io.RawIOBase):
    def __init__(self):
        self.data = b'hello world'
    def readinto(self, b):
        read_len = min(len(self.data), len(b))
        b[:read_len] = self.data[:read_len]
        self.data = self.data[read_len:]
        return read_len

f = File()
print(f.readline())
