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
        self.buffer = None
        self.buffer_size = 0
        self.buffer_pos = 0
        self.buffer_text = False
        self.encoding = 'utf-8'
        self.errors = 'strict'
        self.line_buffering = False
        self.buffer = io.BytesIO()
        self.buffer_size = 0
        self.buffer_pos = 0
        self.buffer_text = False
        self.readable = False
        self.writable = False
        self.seekable = False
        if 'r' in mode:
            self.readable = True
        if 'w' in mode:
            self.writable = True
        if '+' in mode:
