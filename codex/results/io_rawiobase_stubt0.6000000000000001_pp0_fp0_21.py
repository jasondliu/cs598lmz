import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self.__file = file
        super().__init__(*args, **kwargs)

    def close(self):
        self.__file.close()

    def fileno(self):
        return self.__file.fileno()

    def flush(self):
        self.__file.flush()

    def isatty(self):
        return self.__file.isatty()

    def readable(self):
        return self.__file.readable()

    def readline(self, size=-1):
        return self.__file.readline(size)

    def readlines(self, hint=-1):
        return self.__file.readlines(hint)

    def seek(self, offset, whence=io.SEEK_SET):
        return self.__file.seek(offset, whence)

    def seekable(self):
        return self.__file.seekable()

    def tell(self):
        return self.__file.tell()

    def truncate(self,
