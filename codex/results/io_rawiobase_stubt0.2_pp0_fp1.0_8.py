import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self.file = file
        self.mode = mode
        self.pos = 0
        self.closed = False
        self.softspace = 0
        self.newlines = None
        self.encoding = None
        self.errors = None
        self.line_buffering = False
        self.buffer = None
        self.buffer_size = 0
        self.raw = None
        self.readinto = None
        self.read = None
        self.readline = None
        self.readlines = None
        self.write = None
        self.writelines = None
        self.seek = None
        self.tell = None
        self.truncate = None
        self.flush = None
        self.close = None
        self.fileno = None
        self.isatty = None
        self.seekable = None
        self.readable = None
        self.writable = None
        self.__enter__ = None
        self.__exit__ = None
        self.__iter__
