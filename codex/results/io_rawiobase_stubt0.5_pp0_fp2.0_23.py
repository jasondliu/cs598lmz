import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.f = io.open(name, 'rb')
        self.size = os.fstat(self.f.fileno()).st_size

    def read(self, size=-1):
        return self.f.read(size)

    def seek(self, offset, whence=io.SEEK_SET):
        return self.f.seek(offset, whence)

    def tell(self):
        return self.f.tell()

    def close(self):
        return self.f.close()

class Buffer(io.RawIOBase):
    def __init__(self, buffer):
        self.buffer = buffer
        self.size = len(buffer)

    def read(self, size=-1):
        if size == -1:
            size = self.size
        return self.buffer[:size]

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.buffer = self.buffer[offset
