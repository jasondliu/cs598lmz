import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = None
    def open(self):
        self.file = open(self.name, self.mode)
    def close(self):
        self.file.close()
    def read(self, nbytes):
        return self.file.read(nbytes)
    def write(self, data):
        return self.file.write(data)
    def seek(self, pos, whence):
        self.file.seek(pos, whence)
    def tell(self):
        return self.file.tell()
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    def __del__(self):
        self.close()

with File('example.txt', 'w') as f:
    f.write('hello world!')

with File('example.txt', 'r') as f:

