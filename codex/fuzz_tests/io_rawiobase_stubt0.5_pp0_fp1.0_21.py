import io
class File(io.RawIOBase):
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def read(self, n=-1):
        return self.file.read(n)

    def write(self, b):
        return self.file.write(b)

with File('tmp.txt', 'w') as f:
    f.write('hello')
    f.write('bye')

with File('tmp.txt', 'r') as f:
    print(f.read())

# contextlib.contextmanager
from contextlib import contextmanager

@contextmanager
def file(file_name, mode):
    try:
        f = open(file_name, mode)
        yield f
    finally:
        f.close()

with file('tmp
