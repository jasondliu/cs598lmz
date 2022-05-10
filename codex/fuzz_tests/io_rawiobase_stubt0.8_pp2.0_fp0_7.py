import io
class File(io.RawIOBase):
    def __init__(self):
        self.data = b""
        self.offset = 0

    def read(self, size=-1):
        if size >= 0 and len(self.data)-self.offset > size:
            out = self.data[self.offset:self.offset+size]
            self.offset += size
            return out
        else:
            out = self.data[self.offset:]
            self.offset = len(self.data)
            return out

    def write(self, b):
        if self.offset > 0:
            self.data = self.data[:self.offset] + b
            self.offset += len(b)
        else:
            self.data = self.data + b

    def seek(self, offset, whence=0):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset += offset
        elif whence == io.SEEK_END:
            self.offset = len(self.data) + offset

