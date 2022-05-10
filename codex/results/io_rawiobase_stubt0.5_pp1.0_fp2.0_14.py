import io
class File(io.RawIOBase):
    def __init__(self, file, mode='rb', closefd=True):
        if not isinstance(file, io.RawIOBase):
            file = io.FileIO(file, mode=mode)
        self.__file = file
        self.__mode = mode
        self.__closefd = closefd
        self.closed = False

    def close(self):
        if not self.closed:
            self.__file.close()
            self.closed = True

    def fileno(self):
        return self.__file.fileno()

    def readable(self):
        return 'r' in self.__mode

    def readinto(self, b):
        return self.__file.readinto(b)

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        return self.__file.seek(offset, whence)

    def tell(self):
        return self.__file.tell()

    def writable(self):
        return 'w' in self.__mode

   
