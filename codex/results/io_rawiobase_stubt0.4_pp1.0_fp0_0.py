import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.opener = opener
        self.encoding = encoding
        self.errors = errors
        self.newlines = newline
        self.softspace = False
        self.mode = mode
        self.closefd = closefd
        self.opener = opener
        self.encoding = encoding
        self.errors = errors
        self.newlines = newline
        self.softspace = False
        self.closed = False
        self.fd = None
        self.__enter__ = self.open
        self.__exit__ = self.close
        self.__iter__ = self.iter
        self.__next__ = self.next
        self.__enter__ = self.open
        self.__exit__ = self.close
        self.__iter__ = self.iter
        self.
