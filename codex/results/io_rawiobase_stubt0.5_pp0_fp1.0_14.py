import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r'):
        self._path = path
        self._mode = mode
        self._pos = 0
        self._file = None
        self._buffer = None
        self._buffer_pos = 0
        self._buffer_size = 0
        self._buffer_start = 0
        self._buffer_end = 0
        self._newlines = None
        self._update_newlines()
        self._read_ahead = 0
        self._read_buf = None
        self._read_buf_size = 0
        self._read_buf_pos = 0
        self._read_buf_end = 0
        self._read_buf_extra = None
        self._read_buf_extra_pos = 0
        self._read_buf_extra_end = 0
        if self._mode not in ('r', 'rb'):
            raise ValueError("mode must be 'r' or 'rb'")
        if self._mode == 'r':
            self._read_buf_size = io.DEFAULT_BUFFER_SIZE
        self
