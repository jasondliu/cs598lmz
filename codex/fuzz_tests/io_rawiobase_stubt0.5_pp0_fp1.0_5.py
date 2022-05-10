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
    def read(self, size):
        return self.file.read(size)
    def write(self, data):
        self.file.write(data)
    def seek(self, offset, whence):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, type, value, traceback):
        self.close()

with File('my_file.txt', 'w') as f:
    f.write('Hello!')

class File2(io.IOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

