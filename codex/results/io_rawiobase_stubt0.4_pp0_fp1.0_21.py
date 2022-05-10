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
        self._file = None
        self._fd = None
        self._is_text = False
        self._is_binary = False
        self._is_closed = False
        self._should_close = False
        self._encoding_set = False
        self._encoding_bytes = None
        self._encoding_str = None
        self._decoder = None
        self._decoder_for_read = None
        self._decoded_chars = ''
        self._decoded_chars_used = 0
        self._readuniversal = False
        self._readtranslate = None
        self._readnl = None

