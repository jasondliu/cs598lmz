import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r"):
        self.file = file
        self.mode = mode
        self.name = getattr(file, "name", None)
        self.closed = False
        self.softspace = 0
        self.encoding = None
        self.errors = None
        self.newlines = None
        self.line_buffering = False
        self.seekable = getattr(file, "seekable", None)
        self.readable = getattr(file, "readable", None)
        self.writable = getattr(file, "writable", None)
        self.tell = getattr(file, "tell", None)
        self.fileno = getattr(file, "fileno", None)
        self.flush = getattr(file, "flush", None)
        self.isatty = getattr(file, "isatty", None)
        self.read = getattr(file, "read", None)
        self.readline = getattr(file, "readline", None)
        self.readlines
