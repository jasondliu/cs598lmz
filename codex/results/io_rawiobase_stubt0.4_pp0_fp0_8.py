import io
class File(io.RawIOBase):
    def __init__(self, name, mode, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self._name = name
        self._mode = mode
        self._encoding = encoding
        self._errors = errors
        self._newline = newline
        self._closefd = closefd
        self._opener = opener
        self._fd = None
        self._tell = None
        self._io = None
        self._encoder = None
        self._decoder = None
        self._line_buffering = False
        self._readuniversal = False
        self._readtranslate = False
        self._readnl = None
        self._writetranslate = False
        self._writenl = None
        self._seekable = None
        self._writable = None
        self._binary = None
        self._append_mode = False
        self._universal_newline = False
        self._closed = False
        self._close = None
        self._finalizing = False
        self._blksize = DEFAULT_
