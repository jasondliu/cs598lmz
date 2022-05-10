import io
class File(io.RawIOBase):
    def readinto(self, buf):
        return len(buf)
    def close(self):
        pass
    def read(self):
        return b"abc"

d = io.BytesIO
