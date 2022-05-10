import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r', closefd=True):
        if not isinstance(file, int):
            raise TypeError("invalid file: %r" % file)
        self._closefd = closefd
        self.mode = mode
        self.file = file
        self.readable = 'r' in mode
        self.writable = 'w' in mode
        self.seekable = True
        if 'a' in mode:
            self.seek(0, 2)
    def __repr__(self):
        return "<_rawffi.File object file=%d mode=%s>" % (self.file, self.mode)
    def close(self):
        if self._closefd:
            _rawffi.get_os().close(self.file)
            self.file = -1
    def seek(self, offset, whence=0):
        return _rawffi.get_os().lseek(self.file, offset, whence)
    def flush(self):
        pass
    def fileno(self):
       
