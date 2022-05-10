import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', closefd=True):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.fd = os.open(name, os.O_RDONLY)
        self.readable = True
        self.writable = False
        self.seekable = True
        self.closed = False
        self.mode = mode
        self.encoding = None
        self.newlines = None
        self.line_buffering = False
        self.__next = 0
        self.__buf = b''
        self.__buf_len = 0
        self.__buf_pos = 0
        self.__buf_eof = False
        self.__buf_eof_pos = 0
        self.__buf_eof_len = 0
        self.__buf_eof_next = 0
        self.__buf_eof_buf = b''
        self.__buf_eof_buf_len = 0
        self.__buf_eof_buf_pos =
