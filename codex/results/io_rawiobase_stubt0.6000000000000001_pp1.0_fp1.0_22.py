import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.position = 0
        self.end = 0
        self.closed = False
        self.buffer = None
        self.buffer_size = 0
        self.buffer_pos = 0
        self.buffer_end = 0
        self.buffer_start = 0
        self.fd = -1
        self.encoding = None
        self.errors = None
        self.newlines = None
        self.line_buffering = False
        self.closed = False
        self.softspace = False
        self.mode = mode
        self.name = name
        self.fd = -1
        self.position = 0
        self.buffer = None
        self.buffer_size = 0
        self.buffer_pos = 0
        self.buffer_end = 0
        self.buffer_start = 0
        self.softspace = False
        self.line_buffering = False
        self.encoding = None
        self.errors = None
        self.
