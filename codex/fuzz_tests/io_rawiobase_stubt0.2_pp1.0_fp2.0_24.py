import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def close(self):
        return self.file.close()
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True

class FileWrapper(object):
    def __init__(self, file):
        self.file = file
    def __getattr__(self, name):
        return getattr(self.file, name)
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.file.close()

def open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True,
