import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b'\x00'*n
    def write(self, b):
        return len(b)
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return 0
    def tell(self):
        return 0
    def close(self):
        pass

class _FileIO(File):
    @property
    def name(self):
        return '<file>'
    def fileno(self):
        return -1
    def isatty(self):
        return False
    def flush(self):
        pass
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def __repr__(self):
        return '<_io.FileIO name=%r mode=%r>' % (self.name, self.mode)

class BytesIO(_FileIO):
    def __init__(self, initial_bytes=None):
        self._
