import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.file = open(path, mode)
    def readinto(self, buf):
        return self.file.readinto(buf)
    def write(self, buf):
        self.file.write(buf)

f = File('test.txt', 'r')
f.readinto(bytearray(4))

f = File('test.txt', 'w')
f.write(b'abc')

class File:
    def __init__(self, path, mode):
        self.file = open(path, mode)
    def __getattr__(self, name):
        return getattr(self.file, name)
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, tb):
        self.file.close()
        if exc_type is not None:
            raise

with File('test.txt', 'r') as f:
    print(f.read())

class File:
    def __init__
