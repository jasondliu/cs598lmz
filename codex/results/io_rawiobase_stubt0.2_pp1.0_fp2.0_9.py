import io
class File(io.RawIOBase):
    def __init__(self, file, mode='rb', closefd=True):
        self._file = file
        self._mode = mode
        self._closefd = closefd
        self._closed = False
        self._readable = 'r' in mode
        self._writable = 'w' in mode
        self._seekable = 'r' in mode
        self._offset = 0
        self._size = 0
        self._buffer = b''
        self._buffersize = 4096
        self._bufferoffset = 0
        self._bufferlimit = 0
        self._bufferdirty = False
        self._bufferreadonly = False
        self._bufferseekable = False
        self._bufferwritable = False
        self._bufferflushable = False
        self._bufferflushable = False
        self._bufferflushable = False
        self._bufferflushable = False
        self._bufferflushable = False
        self._bufferflushable = False
        self._bufferflushable = False
        self._bufferflushable = False
        self._bufferflushable = False
        self._bufferflushable =
