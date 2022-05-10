import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.__f = f
        self.__size = os.fstat(self.fd)

    def seekable(self):
        return True

    def readable(self):
        return True

    def readinto(self, b):
        n = len(b)
        try:
            res = self.__f.read(n)
        except BlockingIOError:
            return None
        if res is None:
            return None
        b[:len(res)] = res
        return len(res)

    def read(self, n=-1):
        if n is None:
            n = -1
        res = bytearray(n)
        l = self.readinto(res)
        return memoryview(res)[:l].tobytes() if l &gt;= 0 else l

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            offset = min(offset, self.__size)
        elif whence == io.SEE
