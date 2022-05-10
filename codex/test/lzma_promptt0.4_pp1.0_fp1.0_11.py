import lzma
# Test LZMADecompressor with a non-seekable file.

class MyFile:
    def __init__(self, data):
        self.data = data
        self.pos = 0
    def read(self, size):
        if self.pos >= len(self.data):
            return b""
        if size is None or size < 0:
            size = len(self.data) - self.pos
        else:
            size = min(size, len(self.data) - self.pos)
        data = self.data[self.pos:self.pos+size]
        self.pos += size
        return data
    def seek(self, offset, whence=0):
        if whence == 0:
            self.pos = offset
        elif whence == 1:
            self.pos += offset
        elif whence == 2:
            self.pos = len(self.data) + offset
        else:
            raise ValueError("whence must be 0, 1 or 2")
    def tell(self):
        return self.pos

