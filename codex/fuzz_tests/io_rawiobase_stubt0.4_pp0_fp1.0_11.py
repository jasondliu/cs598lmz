import io
class File(io.RawIOBase):
    def __init__(self, filepath, mode):
        self.file = open(filepath, mode)
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, b):
        self.file.write(b)
    def close(self):
        self.file.close()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

with File('test.txt', 'w') as f:
    f.write('hello world')

class File(io.IOBase):
    def __init__(self, filepath, mode):
        self.file = open(filepath, mode)
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, b):
        self.file.write(b)
    def close(self):
        self.file.close()
    def __enter__(self):
        return self
   
