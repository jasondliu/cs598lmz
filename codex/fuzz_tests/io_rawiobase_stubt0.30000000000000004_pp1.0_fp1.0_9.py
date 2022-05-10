import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self._fd = None
        self._closefd = closefd
        self._opener = opener
        self._name = name
        self._mode = mode
        self._encoding = encoding
        self._errors = errors
        self._newlines = None
        self._line_buffering = False
        self._readuniversal = False
        self._writetranslate = False
        self._readtranslate = False
        self._offset = 0
        self._telling = False
        self._textmode = False
        self._fd = None
        self._closefd = closefd
        self._opener = opener
        self._name = name
        self._mode = mode
        self._encoding = encoding
        self._errors = errors
        self._newlines = None
        self._line_buffering = False
        self._readuniversal = False
        self._writetranslate = False
        self._read
