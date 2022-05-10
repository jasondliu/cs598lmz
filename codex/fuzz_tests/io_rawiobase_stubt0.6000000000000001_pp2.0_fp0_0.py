import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.file = file
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        self.name = file
        self.isatty = False
        self.seekable = True
        self.readable = True
        self.writable = True
        self.closed = False
        self.fileno = file
        self.flush = lambda: None
        self.tell = lambda: file.get_offset()
        self.seek = file.seek
        self.truncate = file.truncate
        if mode.find("r") != -1:
            self.read = file.read
        if mode.find("w") != -1:
            self.write = file.write
        if mode.find("
