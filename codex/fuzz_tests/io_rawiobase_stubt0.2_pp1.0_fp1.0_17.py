import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r', closefd=True):
        self._file = file
        self._mode = mode
        self._closefd = closefd
        self._readbuffer = ''
        self._writebuffer = ''
        self._offset = 0
        self._pos = 0
        self._read_lock = threading.Lock()
        self._write_lock = threading.Lock()
        self._seek_lock = threading.Lock()
    def read(self, size=-1):
        with self._read_lock:
            if size < 0:
                size = len(self._readbuffer)
            else:
                size = min(size, len(self._readbuffer))
            data = self._readbuffer[:size]
            self._readbuffer = self._readbuffer[size:]
            self._pos += size
            return data
    def write(self, data):
        with self._write_lock:
            self._writebuffer += data
            self._pos += len(data)
            return len(data)
    def seek(self,
