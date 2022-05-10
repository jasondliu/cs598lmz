import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self._file = file
        super(File, self).__init__(*args, **kwargs)
    def close(self):
        self._file.close()
        return super(File, self).close()
    def fileno(self):
        return self._file.fileno()
    def isatty(self):
        return self._file.isatty()
    def readable(self):
        return self._file.readable()
    def readline(self, size=-1):
        return self._file.readline(size)
    def readlines(self, hint=-1):
        return self._file.readlines(hint)
    def seek(self, offset, whence=os.SEEK_SET):
        return self._file.seek(offset, whence)
    def seekable(self):
        return self._file.seekable()
    def tell(self):
        return self._file.tell()
    def writable(self):
        return self._file.writable()

