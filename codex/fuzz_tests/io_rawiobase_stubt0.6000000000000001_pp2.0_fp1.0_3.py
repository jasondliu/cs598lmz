import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r'):
        self.__file = open(path, mode)

    def close(self):
        self.__file.close()

    def readable(self):
        return self.__file.readable()

    def writable(self):
        return self.__file.writable()

    def seekable(self):
        return self.__file.seekable()

    def readinto(self, b):
        return self.__file.readinto(b)

    def read(self, n=-1):
        return self.__file.read(n)

    def write(self, b):
        return self.__file.write(b)

    def seek(self, offset, whence=io.SEEK_SET):
        return self.__file.seek(offset, whence)

    def tell(self):
        return self.__file.tell()

    def flush(self, path):
        return self.__file.flush(path)

    def truncate(self, size=None):
        return self.__file
