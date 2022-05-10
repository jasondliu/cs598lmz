import io
class File(io.RawIOBase):
    def __init__(self, file, mode="rb", bufsize=-1):
        self.file = file
        self.mode = mode
        self.name = getattr(file, "name", None)
        self.closefd = getattr(file, "closefd", False)
        self.readable = "r" in mode
        self.writable = "w" in mode or "+" in mode
        self.seekable = getattr(file, "seekable", False)
        self.raw = io.RawIOBase
        self.__size = 0
        self.__pos = 0
        self.__buf = []
        self.__bufsize = bufsize
        self.__wbuf = []
        self.__rbuf = []

    def __getattr__(self, item):
        return getattr(self.file, item)

    def readinto(self, b):
        if self.__bufsize > 0 and self.__buf:
            b[:self.__bufsize] = self.__buf
            self.__buf = self.__buf[self
