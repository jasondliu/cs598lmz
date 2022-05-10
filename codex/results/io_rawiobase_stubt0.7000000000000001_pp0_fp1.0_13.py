import io
class File(io.RawIOBase):

    def __init__(self, fp):
        self._fp = fp
        self._size = os.fstat(fp.fileno()).st_size

    @property
    def size(self):
        return self._size

    def readinto(self, b):
        n = self._fp.readinto(b)
        self._size -= n
        return n

    def readable(self):
        return True

file = File(open('file1', 'rb'))

print(file.readinto(bytearray(4)))
print(file.size)
print(file.readinto(bytearray(4)))
print(file.size)

class ReadableFile(io.RawIOBase):

    def __init__(self, filename):
        self._file = open(filename, 'rb')
        self._size = os.fstat(self._file.fileno()).st_size

    @property
    def size(self):
        return self._size

    def readinto(self, b):
        n = self._file.
