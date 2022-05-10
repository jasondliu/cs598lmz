import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.__file = io.FileIO(filename, mode)

    def close(self):
        return self.__file.close()

    def readinto(self, buf):
        return self.__file.readinto(buf)

    def readable(self):
        return self.__file.readable()

    def writable(self):
        return self.__file.writable()

    def seekable(self):
        return self.__file.seekable()

    def seek(self, pos, whence=io.SEEK_SET):
        return self.__file.seek(pos, whence)

    def tell(self):
        return self.__file.tell()

    def read(self, n=-1):
        return self.__file.read(n)

    def write(self, b):
        return self.__file.write(b)
f = File('/tmp/test.txt', 'r')
print(f.read())
f.close()

f = File('/tmp/
