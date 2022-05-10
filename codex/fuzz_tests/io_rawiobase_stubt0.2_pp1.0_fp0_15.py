import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def write(self, b):
        self.file.write(b)
    def writable(self):
        return True
    def close(self):
        self.file.close()

def open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    if 'b' in mode:
        return io.open(file, mode, buffering, encoding, errors, newline, closefd, opener)
    else:
        return io.TextIOWrapper(File(io.open(file, mode + 'b', buffering, encoding,
