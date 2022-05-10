import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r", buffering=-1, encoding=None,
                 errors=None, newline=None, closefd=True, opener=None):
        if isinstance(file, int):
            file = io.open(file, mode, buffering)
        if not closefd:
            file = io.FileIO(file.fileno(), mode)
        io.RawIOBase.__init__(self)
        self._file = file
        self._mode = mode
        self._name = getattr(file, 'name', None)
        self._encoding = encoding
        self._errors = errors
        self._newlines = None
        self._line_buffering = buffering == 1
        self._close = closefd
        self._close_check = False
        self._seekable = file.seekable()
        self._readable = 'r' in mode
        self._writable = 'w' in mode or 'a' in mode
        self._universal_newlines = False
        self._file_closed = False
        self._blksize
