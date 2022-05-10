import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = None
        self.mode = None
    def open(self, mode="r"):
        self.mode = mode
        self.file = open(self.name, mode="r")
        return self
    def read(self, size=-1):
        if "r" not in self.mode:
            raise io.UnsupportedOperation("not readable")
        if size < 0:
            return self.file.read()
        else:
            return self.file.read(size)
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def __enter__(self):
        if self.file is None:
            self.open()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb
