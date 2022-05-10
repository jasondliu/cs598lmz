import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        return self.file.write(b)
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def flush(self):
        return self.file.flush()
    def close(self):
        return self.file.close()

with File('test.txt', 'w') as f:
    f.write('hello, world!')

with File('test.txt', 'r') as f:
    print(f.
