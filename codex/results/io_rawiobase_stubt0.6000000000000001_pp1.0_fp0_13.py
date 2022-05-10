import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.file = open(path, mode)
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self.close()
    def read(self, size=-1):
        return self.file.read(size)
    def readline(self, size=-1):
        return self.file.readline(size)
    def write(self, b):
        return self.file.write(b)
    def close(self):
        return self.file.close()
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def __iter__(self):
        return self
    def __next__(self):
        line = self.readline()
        if not line:
            raise StopIteration
        return line
    def __getattr__(self, name
