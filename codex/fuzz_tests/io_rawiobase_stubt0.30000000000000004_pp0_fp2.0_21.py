import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r"):
        self.file = file
        self.mode = mode
        self.name = file.name
        self.closed = False
        self.softspace = 0
        self.newlines = None
        self.encoding = None
        self.errors = None
        self.line_buffering = False
        self.seekable = True
        self.readable = True
        self.writable = True
        self.readinto = None
        self.read1 = None
        self.write = None
        self.tell = None
        self.flush = None
        self.fileno = None
        self.isatty = None
        self.seek = None
        self.truncate = None
        self.close = None
        self.readable = None
        self.writable = None
        self.seekable = None
        self.read = None
        self.readinto1 = None
        self.readall = None
        self.readinto = None
        self.read1 = None
        self.readable =
