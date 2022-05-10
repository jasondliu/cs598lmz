import io
class File(io.RawIOBase):
    def __init__(self, filename, mode="r", bufsize=-1):
        self.name = filename
        self.mode = mode
        self.closefd = True
        self.encoding = None
        self.errors = None
        self.newlines = None
        self.line_buffering = False
        self.closefd = closefd
        self.pos, self.closed = 0, False
        self.readable = "r" in mode
        self.writable = "w" in mode or "a" in mode
        if bufsize < 0:
            bufsize = DEFAULT_BUFFER_SIZE
        self.buffer = io.BytesIO()
        self.raw = None

        if "b" not in mode:
            self.mode += "b"
        if self.readable:
            self.raw = open(filename, "rb", bufsize)
        if self.writable:
            self.raw = open(filename, self.mode, bufsize)

    def readable(self):
        return self.readable

    def writable(self):
        return self
