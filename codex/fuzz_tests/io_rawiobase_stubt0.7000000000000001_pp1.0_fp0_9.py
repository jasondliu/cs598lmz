import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read()
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)

class FileWrapper(object):
    def __init__(self, file):
        self.file = file
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    @property
    def closed(self):
        return self.file.closed
    def close(self):
        self.file.close()
    def fileno(self):
        return self.file.fileno()
    def flush(self):
        return self.file.flush()
    def isatty(self):
        return self.file.isatty()
    def read(self, n=-
