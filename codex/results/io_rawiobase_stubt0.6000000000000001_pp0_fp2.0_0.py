import io
class File(io.RawIOBase):
    def __init__(self, path, mode="r", buffering=-1, encoding=None,
                 errors=None, newline=None, closefd=True, opener=None):
        """Open file path and assign it to self."""
        self._block_size = io.DEFAULT_BUFFER_SIZE
        self._closed = False
        self._closefd = closefd
        self._encoding = encoding
        self._errors = errors
        self._mode = mode
        self._newlines = None
        self._pos = 0
        self._read_all_done = False
        self._reading = 'r' in mode
        self._seekable = None
        self._universal_newlines = False
        self._writable = 'w' in mode or 'a' in mode

        if not isinstance(path, (bytes, str)):
            raise TypeError("invalid path type: %r" % type(path))
        if not isinstance(mode, str):
            raise TypeError("invalid mode: %r" % mode)
        if not isinstance(buffering,
