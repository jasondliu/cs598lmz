import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='rb'):
        self.filename = filename
        self.mode = mode
        self.file = None
    def close(self):
        self.file.close()
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self.close()
    def __del__(self):
        self.close()
    def readable(self):
        return True
    def writable(self):
        return True
    def read(self, size=-1):
        if self.file is None:
            self.file = open(self.filename, self.mode)
        return self.file.read(size)
    def write(self, b):
        if self.file is None:
            self.file = open(self.filename, self.mode)
        return self.file.write(b)
    def tell(self):
        if self.file is None:
            self.file = open(self.filename, self.mode)
        return self.file.
