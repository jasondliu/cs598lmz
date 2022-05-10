import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.name = name
        self.mode = mode
        self.encoding = encoding
        self.errors = errors
        self.newlines = newline
        self.closefd = closefd
        self.opener = opener
        self.closed = False
        self.__fd = None
        self.__fd_mode = None
        self.__fd_flags = None
        self.__fd_pos = None
        self.__fd_name = None
        self.__fd_encoding = None
        self.__fd_errors = None
        self.__fd_newlines = None
        self.__fd_closefd = None
        self.__fd_opener = None
        self.__fd_closed = None
        self.__fd_readable = None
        self.__fd_writable = None
        self.__fd_seekable = None
        self.__fd_fil
