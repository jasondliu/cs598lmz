import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r', buffering=-1, encoding=None,
                 errors=None, newline=None, closefd=True):
        self.name = filename
        self.mode = mode
        self.closefd = closefd
        self.file = None
        self.readable = 'r' in mode
        self.writable = 'w' in mode or 'a' in mode
        self.seekable = 'r' in mode
        self.fileno = None
        self.flush_needed = False
        self.seek_position = 0
        self.encoding = None
        self.errors = None
        self.newlines = None
        self.line_buffering = False
        self.softspace = False
        self.closed = False
        self.__fd = None

    def open(self, filename, mode='r', buffering=-1, encoding=None,
             errors=None, newline=None, closefd=True):
        self.name = filename
        self.mode = mode
        self.closefd = closefd
       
