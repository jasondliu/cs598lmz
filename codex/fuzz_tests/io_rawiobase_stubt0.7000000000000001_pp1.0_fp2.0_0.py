import io
class File(io.RawIOBase):
    """
    Any object that implements a read() method (such as a file handle or StringIO)
    can be passed to a file_like_object argument.
    """
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = io.open(self.path, mode="rb")
        return self

    def __exit__(self, *args):
        self.file.close()

    def read(self, size=-1):
        return self.file.read(size)

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def readline(self, size=-1):
        return self.file.readline(size)

    def readlines(self, hint=-1):
        return self.file.readlines(hint
