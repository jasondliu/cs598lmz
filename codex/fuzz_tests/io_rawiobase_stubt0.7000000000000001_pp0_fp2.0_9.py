import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.__name = name
        self.__mode = mode
        self.__file = open(name, mode)
    def close(self):
        self.__file.close()
    @property
    def closed(self):
        return self.__file.closed
    def fileno(self):
        return self.__file.fileno()
    def flush(self):
        self.__file.flush()
    def isatty(self):
        return self.__file.isatty()
    def readable(self):
        return self.__mode in {'r', 'r+', 'rb'}
    def readline(self, *args):
        return self.__file.readline(*args)
    def readlines(self, *args):
        return self.__file.readlines(*args)
    def seekable(self):
        return True
    def seek(self, position, whence=0):
        self.__file.seek(position, whence)
    def tell(self
