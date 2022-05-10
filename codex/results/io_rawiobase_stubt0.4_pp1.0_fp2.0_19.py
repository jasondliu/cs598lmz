import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.file = open(filename, mode)
    def write(self, b):
        self.file.write(b)
    def read(self, n):
        return self.file.read(n)
    def close(self):
        self.file.close()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

with File('test.txt', 'w') as f:
    f.write('hello world')

with File('test.txt', 'r') as f:
    print(f.read())
