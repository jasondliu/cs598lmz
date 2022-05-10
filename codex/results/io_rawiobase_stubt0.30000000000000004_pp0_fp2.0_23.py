import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', *, dir_fd=None, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        super().__init__()
        self._closefd = closefd
        self._name = name
        self._mode = mode
        self._encoding = encoding
        self._errors = errors
        self._newline = newline
        self._opener = opener
        self._dir_fd = dir_fd
        self._fd = None
        self._offset = 0
        self._size = 0
        self._buffer = None
        self._buffer_size = 0
        self._buffer_offset = 0
        self._buffer_start = 0
        self._buffer_end = 0
        self._buffer_pos = 0
        self._buffer_dirty = False
        self._buffer_readonly = False
        self._buffer_text = False
        self._buffer_writable = False
        self._buffer_encoding = None
        self._buffer_errors = None
        self._buffer_new
