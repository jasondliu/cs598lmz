import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.fd = open(path, 'rb')
        self.offset = 0
    def read(self, size=-1):
        self.fd.seek(self.offset)
        data = self.fd.read(size)
        self.offset += len(data)
        return data
    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = self.size + offset
    def tell(self):
        return self.offset
    @property
    def size(self):
        return os.path.getsize(self.fd.name)
    def close(self):
        self.fd.close()

def get_file_size(path):
    return os.path.getsize(path)

def get_file_partition(path, size):
    if size <= 0:
        return None
    file_size = get_file_size(
