import io
class File(io.RawIOBase):
    def read(self, n=-1):
        pass
    def readinto(self, b):
        pass
    def write(self, b):
        pass
    def seek(self, offset, whence=0):
        pass
    def tell(self):
        pass
    def fileno(self):
        pass
    def flush(self):
        pass
    def close(self):
        pass
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_value, traceback):
        pass

class TextIOWrapper(io.TextIOBase):
    def read(self, n=-1):
        pass
    def readline(self, limit=-1):
        pass
    def write(self, s):
        pass
    def seek(self, offset, whence=0):
        pass
    def tell(self):
        pass
    def truncate(self, pos=None):
        pass
    def flush(self):
        pass
    def close(self):
        pass
    def __enter__(self
