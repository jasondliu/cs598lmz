import io
# Test io.RawIOBase and friends

# First, a class that simulates a file object
class FileIO(io.RawIOBase):
    def __init__(self, initial_bytes=b''):
        self._buf = io.BytesIO(initial_bytes)
    def readable(self): return True
    def writable(self): return True
    def seekable(self): return True
    def readinto(self, b):
        return self._buf.readinto(b)
    def write(self, b):
        return self._buf.write(b)
    def seek(self, pos, whence=0):
        return self._buf.seek(pos, whence)
    def tell(self):
        return self._buf.tell()
    def fileno(self):
        return None

# A file-like object that doesn't implement truncate()
class NonTruncatingFileIO(FileIO):
    def truncate(self, size=None):
        raise io.UnsupportedOperation("truncate() not supported")

# A file-like object that doesn't implement truncate() or tell()
