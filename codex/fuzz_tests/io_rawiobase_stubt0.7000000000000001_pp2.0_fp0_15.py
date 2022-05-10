import io
class File(io.RawIOBase):
    def read(self, n= -1):
        pass
    def write(self, b):
        pass
    def fileno(self):
        return 0
    def seek(self, pos, whence=0):
        pass
    def tell(self):
        return 0
    def truncate(self, size=None):
        pass
    def close(self):
        pass
    def flush(self):
        pass
    def readinto(self, b):
        pass
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def __iter__(self):
        return self
    def __next__(self):
        return ''
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    def isatty(self):
        return False
    def fileno(self):
        return 0
    def mode(self):
        return ''
    def name(self):
       
