import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.name = name
        self.mode = mode
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        self.fd = None
        self.close()
        if buffering < 0:
            buffering = io.DEFAULT_BUFFER_SIZE
        if buffering == 0:
            if not self.readable() or self.writable():
                raise ValueError('File not open for reading or writing')
            self.raw = True
            self.buffer = None
            self.line_buffering = False
        else:
            if self.readable():
                self.buffer = io.BufferedReader(self.fd, buffering)
            if self.writable():
                self.buffer = io.BufferedWriter(self.fd, buffering)
            self.raw = False
