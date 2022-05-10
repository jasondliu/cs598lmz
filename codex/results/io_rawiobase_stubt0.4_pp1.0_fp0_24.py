import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', bufsize=-1):
        self.name = name
        self.mode = mode
        self.closed = False
        self.softspace = 0
        self.mode = mode
        self.encoding = None
        self.errors = None
        self.newlines = None
        self.line_buffering = False
        self.buffer = io.BytesIO()
        self.buffer.write(open(name, mode).read())
        self.buffer.seek(0)
        self.buffer.name = name
        self.buffer.mode = mode
        self.buffer.closed = False
        self.buffer.softspace = 0
        self.buffer.mode = mode
        self.buffer.encoding = None
        self.buffer.errors = None
        self.buffer.newlines = None
        self.buffer.line_buffering = False
        self.buffer.buffer = None
        self.buffer.raw = None
        self.buffer.closefd = True
        self.buffer.readable = True
        self.buffer.
