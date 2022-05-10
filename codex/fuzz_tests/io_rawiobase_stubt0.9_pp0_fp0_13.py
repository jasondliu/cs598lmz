import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self._file = open(path, mode)

    def seek(self, offset, whence):
        return self._file.seek(offset, whence)

    def flush(self):
        return self._file.flush()

    def read(self, size):
        return self._file.read(size)

    def write(self, buffer):
        return self._file.write(buffer)

    def close(self):
        return self._file.close()

    def detach(self):
        return self._file.detach()

    def readinto(self, bytes_):
        return self._file.readinto(bytes_)

ftest = io.FileIO('/Users/archer/Documents/code/c/test.c')


print(ftest.name)

# with open('/Users/archer/Documents/code/c/test.c','r') as f:
#     print(type(f))
#     print(type(ftest))
#     ftest.close()
#     for line
