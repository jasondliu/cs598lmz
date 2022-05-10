import io
class File(io.RawIOBase):
    """
    A file-like object.
    """
    def __init__(self, file_path, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.file_path = file_path
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        pass

    def fileno(self):
        return 0

    def flush(self):
        pass

    def isatty(self):
        return False

    def readable(self):
        return "r" in self.mode

    def readline(self, size=-1):
        return ""

    def readlines(self, hint=-1):

