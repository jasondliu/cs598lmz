import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def open(self):
        self.file = open(self.filename, self.mode)

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def read(self, size=-1):
        if not self.file:
            self.open()
        return self.file.read(size)

    def write(self, b):
        if not self.file:
            self.open()
        return self.file.write(b)

    def seek(self, offset, whence=io.SEEK_SET):
        if not self.file:
            self.open()
        return self.file.seek(offset, whence)

    def tell(self):
        if not self.file:
            self.open()
        return self.file.tell()

def main():
    f = File('test.txt', 'w')
    f.
