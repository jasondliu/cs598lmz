import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = None
    def open(self):
        self.file = open(self.name, 'rb')
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def readinto(self, b):
        return self.file.readinto(b)
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

with File('test.txt') as f:
    print(f.read())

# 方法二
from contextlib import contextmanager
@contextmanager
def file(name):
    try:
        f = open(name, 'rb')
        yield f
    finally:
        f.close()

with file('test.txt') as f:
    print(f.read())

# 方法三
from contextlib import closing
