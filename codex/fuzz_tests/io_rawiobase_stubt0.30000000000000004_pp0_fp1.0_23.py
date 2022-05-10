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
    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def writeable(self):
        return False
    def writelines(self, lines):
        raise io.UnsupportedOperation
    def write(self, s):
        raise io.UnsupportedOperation
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None

class FileWrapper(object):
    def __init__(self, file, filename=None, headers=None):
        self.file = file
        self.filename = filename
        self.headers = headers or {}
        self.blksize = 4096
        if hasattr(file,
