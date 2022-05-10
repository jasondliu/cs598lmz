import io
class File(io.RawIOBase):
    def __init__(self, f, mode=None):
        pass

    def close(self):
        pass

    def fileno(self):
        return 0

    def flush(self):
        pass

    def isatty(self):
        return False

    def readable(self):
        return False

    def readline(self, size=-1):
        return None

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

class StringIO(io.StringIO):
    def __init__(self, *args, **kwargs):
        pass
