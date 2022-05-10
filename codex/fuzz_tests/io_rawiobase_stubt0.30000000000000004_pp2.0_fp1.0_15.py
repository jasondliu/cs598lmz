import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self._name = name
        self._mode = mode
        self._encoding = encoding
        self._errors = errors
        self._newline = newline
        self._closefd = closefd
        self._opener = opener
        self._closed = False
        self._pos = 0
        self._buf = b''
        self._bufsize = buffering
        self._read_buf = b''
        self._read_buf_size = 0
        self._read_buf_pos = 0
        self._read_buf_len = 0
        self._read_buf_eof = False
        self._write_buf = b''
        self._write_buf_size = 0
        self._write_buf_pos = 0
        self._write_buf_len = 0
        self._write_buf_softspace = False
        self._writable = 'w' in mode or 'a' in mode
