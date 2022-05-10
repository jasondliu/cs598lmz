import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.__f = f
        self.__pos = f.tell()

    def write(self, b):
        self.__f.write(b)
        self.__pos += len(b)

    def seek(self, pos, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.__f.seek(pos, whence)
            self.__pos = self.__f.tell()
            return
        elif whence == io.SEEK_CUR:
            self.__f.seek(self.__pos + pos, io.SEEK_SET)
        elif whence == io.SEEK_END:
            raise io.UnsupportedOperation("Seeking from end not supported")
        else:
            raise io.UnsupportedOperation("Unknown whence value: %r" % (whence,))
        self.__pos = self.__f.tell()

    def tell(self, *args):
        return self.__pos

    def close(self):
        self.__
