import io
class File(io.RawIOBase):
    def __init__(self, filename, mode, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        io.RawIOBase.__init__(self)
        self._file = None
        self.__closed = False
        self.__opener = opener
        self.__closefd = closefd
        if isinstance(filename, (bytes, str)):
            self.__filename = filename
        else:
            self.__filename = None
        self.__mode = mode
        self.__encoding = encoding
        self.__errors = errors
        self.__newline = newline
        self.__line_buffering = False
        self.__read_only = False
        self.__write_only = False
        self.__universal_newlines = False
        self.__read_encoding = None
        self.__read_translate_newlines = False
        self.__read_nl = None
        if self.__filename is not None:
            self._file = self.__opener(self.__filename
