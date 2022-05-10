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
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def write(self, b):
        return self.file.write(b)
    def writable(self):
        return True
    def close(self):
        self.file.close()
    def flush(self):
        self.file.flush()
    def fileno(self):
        return self.file.fileno()
    def isatty(self):
        return self.file.isatty()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return False

import sys
sys.std
