import io
class File(io.RawIOBase):
    """
    A file-like object that reads and writes to a string buffer.
    """
    def __init__(self, buffer=""):
        self._buffer = buffer
        self._pos = 0
        self._closed = False
    def read(self, size=None):
        if self._closed:
            raise ValueError("I/O operation on closed file")
        if size is None:
            res, self._pos = self._buffer[self._pos:], len(self._buffer)
        else:
            res, self._pos = self._buffer[self._pos:self._pos + size], self._pos + size
        return res
    def write(self, b):
        if self._closed:
            raise ValueError("I/O operation on closed file")
        if isinstance(b, unicode):
            b = b.encode("utf-8")
        self._buffer = self._buffer[:self._pos] + b + self._buffer[self._pos + len(b):]
        self._pos += len(b)
        return len(b)
   
