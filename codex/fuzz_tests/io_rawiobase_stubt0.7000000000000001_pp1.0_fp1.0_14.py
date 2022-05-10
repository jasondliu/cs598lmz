import io
class File(io.RawIOBase):
    def __init__(self):
        self.__file = open('test.txt', 'r+')
    def close(self):
        self.__file.close()
    def readable(self):
        return True
    def readinto(self, b):
        return self.__file.readinto(b)
    def writeable(self):
        return True
    def writelines(self, lines):
        return self.__file.writelines(lines)
    def seekable(self):
        return True
    def seek(self, offset, whence):
        return self.__file.seek(offset, whence)
    def tell(self):
        return self.__file.tell()

f = File()
f.tell()
f.seek(0)

f.writeable()

f.seekable()

f.readable()

f.close()

f.readable()

f.readinto(10)

f.writeable()
