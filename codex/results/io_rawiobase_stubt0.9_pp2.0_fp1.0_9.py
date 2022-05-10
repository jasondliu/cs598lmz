import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def write(self, s):
        check_write(s)
    def writable(self):
        return True
    def readable(self):
        return False

class BufferedFile(io.BufferedIOBase):
    def __init__(self, file):
        self._file = file
    def _checkClosed(self):
        if self._file.closed:
            raise ValueError("I/O operation on closed file")
    def write(self, b):
        self._checkClosed()
        check_write(b)
    def writable(self):
        self._checkClosed()
        return True
    def readable(self):
        self._checkClosed()
        return False
    def close(self):
        self._checkClosed()
        self._file.close()

class LineBufferedFile(BufferedFile):
    def write(self, b):
        super().write(b)
        if b.decode("utf-8").endswith("\
