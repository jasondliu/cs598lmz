import io
class File(io.RawIOBase):
    """
    A file-like object that returns a given message when read from.
    """
    def __init__(self, message):
        self.message = message

    def read(self, size=-1):
        if size == -1:
            return self.message
        else:
            return self.message[:size]

    def readline(self, size=-1):
        if size == -1:
            return self.message
        else:
            return self.message[:size]

    def readlines(self, sizehint=-1):
        return [self.message]

    def seek(self, offset, whence=0):
        if offset == 0:
            return
        else:
            raise IOError("Cannot seek")

    def tell(self):
        return 0

    def write(self, s):
        raise IOError("Cannot write")

    def writelines(self, lines):
        raise IOError("Cannot write")

    def truncate(self, size=None):
        raise IOError("Cannot truncate")

    def flush(
