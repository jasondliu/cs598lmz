import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.opener = opener
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.buffering = buffering
        self.closed = False
        self.readable = False
        self.writable = False
        self.seekable = False
        self.isatty = False
        self.line_buffering = False
        self.softspace = False
        self.__open()
    def __open(self):
        if self.mode == 'r':
            self.readable = True
            self.seekable = True
            self.isatty = False
            self.softspace = False
            self.__pos = 0
            self.__buf = 'Hello, world!'
        elif self.mode == 'w':
            self.writ
