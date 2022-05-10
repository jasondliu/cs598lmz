import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r', closefd=True):
        self._filename = filename
        self._mode = mode
        self._closefd = closefd
        self._fd = None
        self._open()
        self._readbuffer = b''
        self._readbufferoffset = 0

    def __del__(self):
        self.close()

    def _open(self):
        if self._fd is not None:
            raise ValueError('I/O operation on closed file')
        if self._mode == 'r':
            self._fd = open(self._filename, 'rb')
        elif self._mode == 'w':
            self._fd = open(self._filename, 'wb')
        elif self._mode == 'a':
            self._fd = open(self._filename, 'ab')

    def _read_chunk(self):
        if self._mode == 'w':
            raise io.UnsupportedOperation('File not open for reading')
        if self._fd is None:
            self._open()
        self._readbuffer =
