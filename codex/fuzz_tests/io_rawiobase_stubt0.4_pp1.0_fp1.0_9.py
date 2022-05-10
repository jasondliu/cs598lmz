import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self.file = file
        self.args = args
        self.kwargs = kwargs
        self.mode = file.mode
        self.name = file.name
        self.closed = file.closed
        self.encoding = file.encoding
        self.errors = file.errors
        self.newlines = file.newlines
        self.softspace = file.softspace
        self.buffer = file.buffer
        self.raw = file.raw
        self.isatty = file.isatty
        self.fileno = file.fileno
        self.close = file.close
        self.flush = file.flush
        self.fileno = file.fileno
        self.isatty = file.isatty
        self.read = file.read
        self.readinto = file.readinto
        self.readline = file.readline
        self.readlines = file.readlines
        self.seek = file.seek
        self.tell = file.tell

