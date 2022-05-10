import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
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
        self.isatty = False
        self.flushable = True
        self.closefd = True
        self.closed = False
        self.mode = mode
        self.name = file.name
        self.softspace = 0
        self.newlines = None
        self.encoding = None
        self.errors = None
        self.line_buffering = False
        self.seekable = True
        self.readable = True
        self.writable = True
        self.isatty = False
        self.flushable = True
        self.closefd = True
        self.closed = False
       
