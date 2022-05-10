import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self.__file = file
        super().__init__(*args, **kwargs)
    def read(self, size=-1):
        return self.__file.read(size)
    def write(self, data):
        return self.__file.write(data)
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        return self.__file.seek(offset, whence)
    def tell(self):
        return self.__file.tell()
    def close(self):
        self.__file.close()
    def flush(self):
        self.__file.flush()
    def fileno(self):
        return self.__file.fileno()
    def isatty(self):
        return self.__file.isatty()
    @property
    def closed(self):
        return self.__file.closed

class Buffer(io.RawIOBase):
    def __init__(self
