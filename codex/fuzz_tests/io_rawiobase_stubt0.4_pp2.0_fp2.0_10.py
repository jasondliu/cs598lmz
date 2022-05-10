import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.closed = False
        self.open()

    def open(self):
        self.file = open(self.filename, self.mode)

    def close(self):
        if self.file:
            self.file.close()
            self.closed = True

    def read(self, size=-1):
        if self.closed:
            self.open()
        return self.file.read(size)

    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def readinto(self, b):
        data = self.read(len(b))
        if not data:
            return None
        b[:len(data)] = data
        return len(data)

def test_file():
    f = File('file.py')
    print(f.read(10))
