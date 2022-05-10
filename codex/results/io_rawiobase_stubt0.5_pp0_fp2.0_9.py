import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self._file = file
        io.RawIOBase.__init__(self, *args, **kwargs)

    def close(self):
        if self._file is not None:
            self._file = None
            return self._file.close()

    def fileno(self):
        return self._file.fileno()

    def flush(self):
        return self._file.flush()

    def isatty(self):
        return self._file.isatty()

    def readable(self):
        return self._file.readable()

    def readline(self, size=-1):
        return self._file.readline(size)

    def readlines(self, hint=-1):
        return self._file.readlines(hint)

    def seek(self, offset, whence=io.SEEK_SET):
        return self._file.seek(offset, whence)

    def seekable(self):
        return self._file.seekable()

    def tell(self):
       
