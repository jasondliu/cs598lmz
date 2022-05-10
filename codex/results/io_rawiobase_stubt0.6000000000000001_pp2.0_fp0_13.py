import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def read(self, size = None):
        return b''
    def write(self, data):
        pass
    def seek(self, offset, whence = io.SEEK_SET):
        pass
    def close(self):
        pass
    def fileno(self):
        return -1
    def flush(self):
        pass
    def isatty(self):
        return False
    def readable(self):
        return False
    def seekable(self):
        return False
    def writable(self):
        return True
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self.close()
class StringIO(io.StringIO):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mode = io.TextIOWrapper.WRITE
    def close(self):
        self.flush()
        self.
