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
        self._offset = 0
        self._softspace = False
    def readable(self):
        return self._reading
    def writable(self):
        return self._writing
    def seekable(self):
        return self._seekable
    def close(self):
        if self._closefd:
            self._file.close()
    def flush(self):
        if self._writing:
            self._file.write(self._writebuffer)
            self._writebuffer = ''
    def tell(self):
        return self._offset
    def seek(self, offset, whence=0):
        if whence == 0:
            self._offset = offset
        elif whence == 1:
