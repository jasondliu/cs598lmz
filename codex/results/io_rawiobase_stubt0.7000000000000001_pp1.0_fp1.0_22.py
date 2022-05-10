import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', encodig=None, errors=None, newline=None):
        pass
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.closed:
            self.close()
    def close(self):
        pass
    def fileno(self):
        pass
    def flush(self):
        pass
    def isatty(self):
        pass
    def read(self, size=-1):
        return self.buffer.read(size)
    def readable(self):
        pass
    def readinto(self, b):
        pass
    def readline(self, size=-1):
        return self.buffer.readline(size)
    def readlines(self, hint=None):
        return self.buffer.readlines(hint)
    def seek(self, offset, whence=0):
        self.buffer.seek(offset, whence)
    def seekable(self):
        pass

