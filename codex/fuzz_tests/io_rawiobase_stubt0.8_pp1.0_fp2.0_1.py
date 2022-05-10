import io
class File(io.RawIOBase):

    def __init__(self, fobj):
        self.fobj = fobj

        # Handle windows file system newlines
        self.newlines = None

    def close(self):
        self.fobj.close()

    def readable(self):
        return False

    def read(self, size=-1):
        raise io.UnsupportedOperation("not readable")

    def readall(self):
        return self.read()

    def readinto(self, b):
        raise io.UnsupportedOperation("not readable")

    def seekable(self):
        return False

    def seek(self, offset, whence=0):
        raise io.UnsupportedOperation("not seekable")

    def tell(self):
        raise io.UnsupportedOperation("not seekable")

    def write(self, b):
        if not self.fobj.writable():
            raise io.UnsupportedOperation("not writable")

        if isinstance(b, str):
            n = self.fobj.write(b)
            return n
        else:
            return io.RawIOBase
