import io
class File(io.RawIOBase):
    """
    This is a stub for the python 3 file type, which is used by the
    pickle module.

    """
    def __init__(self, filename, mode):
        pass

    def close(self):
        pass

    def fileno(self):
        return 0

    def flush(self):
        pass

    def isatty(self):
        return False

    def read(self, n=-1):
        return bytes()

    def readable(self):
        return False

    def readline(self, limit=-1):
        return bytes()

    def readlines(self, hint=-1):
        return []

    def seek(self, offset, whence=io.SEEK_SET):
        pass

    def seekable(self):
        return False

    def tell(self):
        return 0

    def truncate(self, size=None):
        pass

    def writable(self):
        return False

    def write(self, b):
        pass

    def writelines(self, lines):
        pass

class BufferedReader(io.
