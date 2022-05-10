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
        self.write_through = False
        self.writable = 'w' in mode
        self.readable = 'r' in mode
        self.seekable = True
        self.tell = file.tell
        self.seek = file.seek
        self.truncate = file.truncate
        self.flush = file.flush
        self.close = file.close
        self.fileno = file.fileno
        self.isatty = file.isatty
        self.readable = file.readable
        self.writable = file.writable
        self.seekable = file.seekable
        self.read = file.read
        self.readinto = file.readinto
        self.read
