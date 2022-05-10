import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self._fd = open(name, mode)
        self.closed = False
        self.softspace = 0
    def close(self):
        self._fd.close()
        self.closed = True
    def fileno(self):
        return self._fd.fileno()
    def flush(self):
        self._fd.flush()
    def isatty(self):
        return self._fd.isatty()
    def next(self):
        return self._fd.next()
    def read(self, n=-1):
        return self._fd.read(n)
    def readline(self, length=None):
        return self._fd.readline(length)
    def readlines(self, sizehint=0):
        return self._fd.readlines(sizehint)
    def seek(self, offset, whence=0):
        return self._fd.seek(offset, whence)
    def tell(self):
        return self
