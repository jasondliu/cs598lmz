import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r'):
        self.path = path
        self.mode = mode
        self.file = None
        self.open()
    def open(self):
        if self.file is None:
            self.file = open(self.path, self.mode)
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def read(self, size=-1):
        self.open()
        return self.file.read(size)
    def write(self, data):
        self.open()
        return self.file.write(data)
    def seek(self, offset, whence=io.SEEK_SET):
        self.open()
        return self.file.seek(offset, whence)
    def tell(self):
        self.open()
        return self.file.tell()
    def flush(self):
        self.open()
        return self.file.flush()
    def __enter__(self):
        self.open
