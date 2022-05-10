import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r', closefd=True):
        self._file = file
        self._mode = mode
        self._closefd = closefd
        self._reading = 'r' in mode
        self._writing = 'w' in mode
        self._seekable = True
        self._tell = file.tell
        self._seek = file.seek
        self._readinto = file.readinto
        self._read = file.read
        self._write = file.write
        self._flush = file.flush
        self._close = file.close
        self._fileno = file.fileno
        self._isatty = file.isatty
        self._closed = False
    def readable(self):
        return self._reading
    def writable(self):
        return self._writing
    def seekable(self):
        return self._seekable
    def readinto(self, b):
        return self._readinto(b)
    def read(self, n=-1):
        return self._read(n)
    def write(
