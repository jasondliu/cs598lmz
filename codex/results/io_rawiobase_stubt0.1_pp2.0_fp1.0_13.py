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
        self.read_lock = None
        self.write_lock = None
        self.seekable = None
        self.readable = None
        self.writable = None
        self.tell_lock = None
        self.seek_lock = None
        self.readinto_lock = None
        self.read1_lock = None
        self.readinto1_lock = None

