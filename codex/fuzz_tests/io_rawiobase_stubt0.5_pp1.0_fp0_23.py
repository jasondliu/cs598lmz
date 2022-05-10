import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.file = file
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        self.closed = False
        self.softspace = 0
        self.mode = "r"
        self.name = file
        self.encoding = encoding
        self.newlines = None
        self.line_buffering = False
        self.seekable = True
        self.readable = True
        self.writable = False
        self.closed = False

    def close(self):
        if self.closed:
            return
        self.closed = True

    def fileno(self):
        return self.file.fileno()

    def flush(self):
        pass

    def isatty(self):
       
