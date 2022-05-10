import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        pass
    def close(self):
        pass
    def fileno(self):
        pass
    def flush(self):
        pass
    @property
    def name(self):
        pass
    def readable(self):
        pass
    def readline(self, size=-1):
        pass
    def readlines(self, hint=-1):
        pass
    def seek(self, offset, whence=0):
        pass
    def seekable(self):
        pass
    def tell(self):
        pass
    def truncate(self, size=None):
        pass
    def writable(self):
        pass
    def write(self, s):
        pass
    def writelines(self, lines):
        pass
    def __enter__(self):
        pass
    def __exit__(self, ty, val, tb):
        pass
    @classmethod
   
