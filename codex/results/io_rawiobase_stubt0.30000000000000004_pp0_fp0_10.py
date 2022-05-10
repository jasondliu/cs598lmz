import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.fd = None
        self.mode = None
        self.softspace = False
        self.closed = False
        self.newlines = None
        self.encoding = None
        self.errors = None
        self.line_buffering = False
        self.buffer = None
        self.buffer_size = 8192
        self.buffer_pos = 0
        self.buffer_avail = 0
        self.buffer_dirty = False
        self.buffer_text = False
        self.buffer_lines = False
        self.buffer_writable = False
        self.readable = False
        self.writable = False
        self.seekable = False
        self.tell_pos = 0
        self.seek_pos = 0
        self.seek_end = 0
        self.seek_set = 0
        self.seek_cur = 1
        self.seek_end = 2
        self.flush_error = None
        self.flush_lock = None
        self.flush_unlocked
