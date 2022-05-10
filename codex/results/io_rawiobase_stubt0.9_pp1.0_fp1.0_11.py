import io
class File(io.RawIOBase):
    def __init__(self, fd, name=None, mode=None, closefd=True):
        self.__fd = fd
        self.__mode = mode
        if name:
            self.name = name
        else:
            self.name = getattr(fd, 'name', None)
        self.__closefd = closefd
    def __repr__(self):
        return '<%s.%s 0x%x file=%s,closed=%d,mode=%s>' % (__name__,
          self.__class__.__name__, id(self), self.name,
          self.closed, self.__mode)
    def close(self):
        fd = self.__fd
        if self.__closefd:
            fd.close()
    def fileno(self):
        return self.__fd.fileno()
    def flush(self, *args):
        return self.__fd.flush(*args)
    def isatty(self):
        return self.__fd.isatty()

