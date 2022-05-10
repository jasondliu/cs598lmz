import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = None
        self.open()
    def open(self):
        self.file = open(self.name, self.mode)
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, data):
        return self.file.write(data)
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def flush(self):
        return self.file.flush()
    def fileno(self):
        return self.file.fileno()
    def isatty(self):
        return self.file.isatty()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close
