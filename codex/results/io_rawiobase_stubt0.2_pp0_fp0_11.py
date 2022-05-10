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
        self.flushable = False
        self.read1 = None
        self.readinto1 = None
        self.readinto = None
        self.readline = None
        self.readlines = None
        self.write = None
        self.writelines = None
        self.tell = None
        self.seek = None
        self.truncate = None
        self.fileno = None
        self.flush = None
        self.close = None
        self.readable = None
        self.writable = None
        self.seekable = None
        self.is
