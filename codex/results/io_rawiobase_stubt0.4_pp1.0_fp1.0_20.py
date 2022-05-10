import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r', encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.path = path
        self.mode = mode
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        self.fd = None
        self.closed = False
        self.mode = mode
        self.encoding = encoding
        self.errors = errors
        self.newlines = None
        self.line_buffering = False
        self.softspace = False
        self.name = path
        self.mode = mode
        self.encoding = encoding
        self.errors = errors
        self.newlines = None
        self.line_buffering = False
        self.softspace = False
        self.name = path
        self.mode = mode
        self.encoding = encoding
        self.errors = errors
        self.newlines = None
        self.line_buffering = False
