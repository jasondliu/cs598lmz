import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self._path = path
        self._mode = mode
        self._file = None

    def __enter__(self):
        self._file = open(self._path, self._mode)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()

    def read(self, size=-1):
        return self._file.read(size)

    def write(self, b):
        return self._file.write(b)

    def seek(self, offset, whence=io.SEEK_SET):
        return self._file.seek(offset, whence)

    def tell(self):
        return self._file.tell()

# with File('test.txt', 'w') as f:
#     f.write('hello world')

# with File('test.txt', 'r') as f:
#     print(f.read())

# print(f.read())

# with File('test.txt', 'r') as
