import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.path = path
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        self.fd = None
        self._close = None
        self._read = None
        self._seek = None
        self._write = None
        self._fileno = None
        self._io = None
        self._io_init()
    def _io_init(self):
        if self.mode == 'r':
            self._read = self._io.read
            self._seek = self._io.seek
            self._fileno = self._io.fileno
        elif self.mode == 'w':
            self._write = self._io.write
            self._fileno = self._io.fileno
       
