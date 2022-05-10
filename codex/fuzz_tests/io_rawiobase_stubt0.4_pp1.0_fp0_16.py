import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode
        self.file = None
        self.open()

    def open(self):
        if self.file is None:
            self.file = open(self.name, self.mode)

    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None

    def read(self, n=-1):
        return self.file.read(n)

    def write(self, b):
        return self.file.write(b)

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def flush(self):
        return self.file.flush()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self
