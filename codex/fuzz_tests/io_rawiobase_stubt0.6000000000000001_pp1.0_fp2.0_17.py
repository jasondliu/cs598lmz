import io
class File(io.RawIOBase):
    def __init__(self, file, mode = 'r', closefd = True):
        self.closefd = closefd
        self.__file = file
        self.__mode = mode
        self.__closed = False
        self.__encoding = None
        self.__errors = None
        self.__newlines = None
        self.__line_buffering = False
        self.__readahead = None
        self.__isatty = False
        self.__pos = 0
        self.__readable = False
        self.__seekable = False
        self.__writable = False
        self.__write_stack = []
        self.__translate = False
        self.__encoding = 'utf-8'
        self.__errors = 'strict'
        self.__writable = self.__mode == 'w' or self.__mode == 'a'
        self.__readable = self.__mode == 'r' or self.__mode == 'r+'
        self.__seekable = self.__mode == 'r' or self.
