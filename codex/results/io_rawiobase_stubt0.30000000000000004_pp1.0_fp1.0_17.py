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
        self.name = file.name
        self.mode = file.mode
        self.encoding = file.encoding
        self.errors = file.errors
        self.newlines = file.newlines
        self.softspace = file.softspace
        self.buffer = file.buffer
        self.line_buffering = file.line_buffering
        self.readable = file.readable
        self.writable = file.writable
        self.seekable = file.seekable
        self.tell = file.tell
        self.fileno = file.fileno
        self.isatty =
