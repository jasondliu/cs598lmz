import io
class File(io.RawIOBase):
    """A file-like object that writes to a string buffer.
    """
    def __init__(self):
        self.buffer = []
        self.offset = 0
        self.closed = False

    def close(self):
        self.closed = True

    def isatty(self):
        return False

    def readable(self):
        return False

    def writable(self):
        return True

    def seekable(self):
        return True

    def read(self, size=-1):
        raise io.UnsupportedOperation

    def readall(self):
        raise io.UnsupportedOperation

    def readinto(self, b):
        raise io.UnsupportedOperation

    def write(self, b):
        if self.closed:
            raise ValueError('write to closed file')
        self.buffer.append(b)
        return len(b)

    def seek(self, offset, whence=io.SEEK_SET):
        if self.closed:
            raise ValueError('seek on closed file')
        if whence == io.SEEK_SET:

