import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self._filename = filename
        self._file = None

    def __enter__(self):
        self._file = open(self._filename, 'r')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()

    def read(self, size=-1):
        if size < 0:
            return self._file.read()
        else:
            return self._file.read(size)

    def readable(self):
        return True

with File('file.txt') as file:
    print(file.read())

# В примере выше мы создали класс File, который наследуется от io.RawIOBase.
# Это необходимо для того, чт
