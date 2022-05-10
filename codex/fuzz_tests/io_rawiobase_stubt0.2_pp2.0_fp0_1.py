import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r', closefd=True):
        self._file = file
        self._mode = mode
        self._closefd = closefd
        self._reading = 'r' in mode
        self._writing = 'w' in mode
        self._seekable = '+' in mode
        self._readbuffer = ''
        self._writebuffer = ''
        self._pos = 0
        self._closed = False
        self._softspace = False
        self._line_buffering = False
        self._universal_newlines = False
        self._encoding = None
        self._errors = None
        self._decoder = None
        self._readtranslate = None
        self._readuniversal = None
        self._readline = None
        self._writetranslate = None
        self._writeuniversal = None
        self._encoding = 'utf-8'
        self._errors = 'strict'
        self._decoder = codecs.getincrementaldecoder(self._encoding)(self._errors)
        self._readtranslate
