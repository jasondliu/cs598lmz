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
    def writeable(self):
        return False

class FileWrapper(object):
    def __init__(self, file):
        self.file = file
    def __getattr__(self, name):
        return getattr(self.file, name)
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self.file.close()

def open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    if 'b' in mode:
        return FileWra
