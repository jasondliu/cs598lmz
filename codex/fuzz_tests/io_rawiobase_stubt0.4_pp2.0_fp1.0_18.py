import io
class File(io.RawIOBase):
    """
    A file-like object that writes to a file on disk.
    """
    def __init__(self, filepath, mode='wb', buffering=-1, encoding=None,
                 errors=None, newline=None, closefd=True, opener=None):
        self.filepath = filepath
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener

        self.file = None

    def __enter__(self):
        self.file = open(self.filepath, self.mode, self.buffering, self.encoding,
                         self.errors, self.newline, self.closefd, self.opener)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.file = None

    def readable(self):
        return self.file.readable()

    def
