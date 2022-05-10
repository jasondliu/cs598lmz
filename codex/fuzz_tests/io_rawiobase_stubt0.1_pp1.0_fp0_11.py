import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.opener = opener
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.buffering = buffering
        self.__fd = None
        self.__is_open = False
        self.__is_readable = False
        self.__is_writable = False
        self.__is_appending = False
        self.__is_binary = False
        self.__is_text = False
        self.__is_exclusive = False
        self.__is_atty = False
        self.__is_closed = False
        self.__is_seekable = False
        self.__is_blocking = False
        self.__is_line_buffering = False
        self.__is_buffered = False
        self.
