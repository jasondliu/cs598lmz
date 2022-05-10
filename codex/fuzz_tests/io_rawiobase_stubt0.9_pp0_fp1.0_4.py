import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        if not hasattr(file,'read'):
            raise TypeError("invalid file: %r" % file)
        io.RawIOBase.__init__(self)
        self._file = file
    def close(self):
        self._file.close()
    def fileno(self):
        return self._file.fileno()
    def isatty(self):
        return self._file.isatty()
    def readable(self):
        return True
    def readinto(self, b):
        return self._file.readinto(b)
    def seek(self, pos, whence=0):
        return self._file.seek(pos, whence)
    def seekable(self):
        return True
    def tell(self):
        return self._file.tell()
    def writable(self):
        return False


class Part(object):
    def __init__(self, content_type, body, flags, filename=None):
        self.content_type = content
