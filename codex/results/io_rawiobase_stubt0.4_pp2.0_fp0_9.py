import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        return self.file.write(b)
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def readinto(self, b):
        data = self.read(len(b))
        if not data:
            return 0
        b[:len(data)] = data
        return len(data)
    def __getattr__(self, name):
        return getattr(self.file, name)

def open(file, mode="rb", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    if isinstance(file
