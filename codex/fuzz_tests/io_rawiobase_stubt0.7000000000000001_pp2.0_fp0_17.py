import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.__name = name
        self.__mode = mode
        self.__length = os.stat(self.__name).st_size
        self.__offset = 0

    def readinto(self, b):
        count = len(b)
        with open(self.__name, self.__mode) as fd:
            if self.__offset:
                fd.seek(self.__offset)
            s = fd.read(count)
            if not s:
                return 0
            b[:len(s)] = s
            self.__offset += len(s)
            return len(s)
    def tell(self):
        return self.__offset
    def seek(self, offset, whence=0):
        if whence:
            offset += self.__offset
        self.__offset = offset
    def read(self, n=-1):
        with open(self.__name, self.__mode) as fd:
            if self.__offset:
                fd
