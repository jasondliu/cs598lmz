import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.file = io.FileIO(name, mode)
        self.name = name
        self.mode = mode
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, b):
        return self.file.write(b)
    def close(self):
        return self.file.close()
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

def open(name, mode):
    return File(name, mode)
