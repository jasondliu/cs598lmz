import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.open()

    def open(self):
        self.file = open(self.filename, self.mode)

    def close(self):
        self.file.close()

    def read(self, n=-1):
        return self.file.read(n)

    def write(self, b):
        return self.file.write(b)

    def seekable(self):
        return self.file.seekable()

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

f = File('data.txt')
print(f.read())
f.seek(0)
print(f.read())
f.seek(0)
print(f.read())
f.seek(0)
print(f.read())
f.seek(0)
print
