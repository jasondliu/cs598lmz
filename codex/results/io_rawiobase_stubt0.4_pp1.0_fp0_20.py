import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r", buffering=-1, encoding=None,
                 errors=None, newline=None, closefd=True, opener=None):
        self.name = file
        self.mode = mode
        self.closefd = closefd
        self.opener = opener
        self.encoding = encoding
        self.errors = errors
        self.newlines = None
        self.line_buffering = False
        if buffering < 0:
            buffering = io.DEFAULT_BUFFER_SIZE
        self.buffer = io.BytesIO()
        self.buffering = buffering
        self.readable = "r" in mode
        self.writable = "w" in mode
        self.seekable = True
        if self.readable:
            self._read_all_data()
        if newline is not None:
            if "U" in mode:
                raise ValueError("newline is not allowed in universal "
                                 "newline mode")
            else:
                self.newlines = newline

    def _read
