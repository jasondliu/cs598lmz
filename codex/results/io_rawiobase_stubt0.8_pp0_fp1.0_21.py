import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.__name = name
        self.__fp = None
        self.mode = mode
        self.newlines = None
        return
    def close(self):
        self.__fp.close()
        return
    def closed(self):
        return self.__fp.closed
    def fileno(self):
        return self.__fp.fileno()
    def flush(self):
        self.__fp.flush()
        return
    def isatty(self):
        return self.__fp.isatty()
    def readable(self):
        return self.__fp.readable()
    def readline(self, size=-1):
        return self.__fp.readline(size)
    def readlines(self, hint=-1):
        return self.__fp.readlines(hint)
    def seek(self, offset, whence=0):
        return self.__fp.seek(offset, whence)
    def seekable(self):
        return self.__fp.seekable()

