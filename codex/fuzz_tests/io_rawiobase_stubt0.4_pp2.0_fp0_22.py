import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r", buffering=-1, encoding=None,
                 errors=None, newline=None, closefd=True, opener=None):
        self.file = file
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        self.closed = False
        self.name = file
        self.mode = mode
        self.softspace = False
        self.seekable = True
        self.readable = True
        self.writable = False
        self.isatty = False
        self.tell = 0
        self.fileno = file
        self.flush = None
        self.readline = None
        self.readlines = None
        self.writelines = None
        self.read1 = None
        self.readinto = None
        self.readinto1 = None
        self.readall = None
        self.truncate =
