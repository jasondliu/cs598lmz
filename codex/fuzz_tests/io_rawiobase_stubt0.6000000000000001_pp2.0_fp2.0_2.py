import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self._file = file
        io.RawIOBase.__init__(self, *args, **kwargs)
    def close(self):
        if self._file is not None:
            self._file.close()
            self._file = None
    def fileno(self):
        return self._file.fileno()
    def readinto(self, b):
        return self._file.readinto(b)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self._file.seek(offset, whence)
    def tell(self):
        return self._file.tell()
    def writable(self):
        return False


class InputFile(File):
    def __init__(self, file, *args, **kwargs):
        File.__init__(self, file, *args, **kwargs)
        self.buffer = b''
    def readinto(self, b
