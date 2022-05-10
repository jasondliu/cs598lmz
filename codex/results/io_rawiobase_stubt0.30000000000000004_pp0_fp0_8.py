import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.fd = io.open(path, 'rb')
        self.size = os.fstat(self.fd.fileno()).st_size
        self.offset = 0
    def read(self, size=-1):
        if size == -1:
            size = self.size - self.offset
        if size == 0:
            return b''
        self.fd.seek(self.offset)
        data = self.fd.read(size)
        self.offset += len(data)
        return data
    def tell(self):
        return self.offset
    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = self.size + offset
        return self.offset
    def close(self):
        self.fd.close()

def get_file_size(path):
    return os.fstat(
