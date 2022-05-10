import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.file = file
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        self.closed = False
        self.name = file.name
        self.mode = file.mode
        self.readable = file.readable
        self.writable = file.writable
        self.seekable = file.seekable
        self.tell = file.tell
        self.seek = file.seek
        self.truncate = file.truncate
        self.read = file.read
        self.read1 = file.read1
        self.readinto = file.readinto
        self.readinto1 = file.readinto1
        self.readline = file.readline
        self.readlines = file
