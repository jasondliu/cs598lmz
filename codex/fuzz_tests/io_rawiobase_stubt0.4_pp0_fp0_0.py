import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', buffering=-1, encoding=None,
                 errors=None, newline=None, closefd=True, opener=None):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.opener = opener
        if closefd:
            self._closefd = True
        else:
            self._closefd = False
        self._mode = mode
        self._encoding = encoding
        self._errors = errors
        self._newlines = None
        self._line_buffering = False
        if buffering < 0:
            buffering = io.DEFAULT_BUFFER_SIZE
        self._blocking = True
        self._decoded_chars = ''
        self._decoded_chars_used = 0
        self._snapshot = None
        self._readuniversal = False
        self._readtranslate = None
        self._readnl = None
        self._writetranslate = None
        self._seekable = None
        self._tellable = None
        self
