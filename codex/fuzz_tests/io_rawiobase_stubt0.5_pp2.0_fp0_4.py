import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.__path = path
        self.__file = None
        self.__mode = None

    def open(self, mode):
        self.__mode = mode
        self.__file = open(self.__path, mode)

    def close(self):
        self.__file.close()

    def read(self, size=-1):
        return self.__file.read(size)

    def write(self, b):
        self.__file.write(b)
        self.__file.flush()
        return len(b)

    def seek(self, offset, whence=io.SEEK_SET):
        return self.__file.seek(offset, whence)

    def tell(self):
        return self.__file.tell()

    def flush(self):
        pass

f = File(r'D:\test.txt')
f.open('w')
f.write(b'hello')
f.close()

f.open('r')
print(f.read())
f.close
