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
        self.buffer_avail = 0
        self.buffer_view = None
        self.buffer_view_pos = 0
        self.buffer_view_avail = 0
        self.buffer_view_end = 0
        self.read_end = 0
        self.read_pos = 0
        self.read_start = 0
        self.read_pending = 0
        self.read_chunk = 0
        self.read_chunk_size = 0
        self.read_universal = False
        self.read_translate = False
        self.read_nl = None
        self.
