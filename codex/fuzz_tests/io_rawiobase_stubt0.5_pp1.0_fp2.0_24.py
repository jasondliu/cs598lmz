import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self._filename = filename
        self._mode = mode
        self._file = None
    def open(self):
        if self._file is None:
            self._file = open(self._filename, self._mode)

    def close(self):
        if self._file is not None:
            self._file.close()
            self._file = None

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def readable(self):
        return 'r' in self._mode

    def writable(self):
        return 'w' in self._mode

    def readinto(self, b):
        return self._file.readinto(b)

    def write(self, b):
        return self._file.write(b)

f = File('/tmp/file.txt', 'w')
f.write('hello, world')
f.close()

