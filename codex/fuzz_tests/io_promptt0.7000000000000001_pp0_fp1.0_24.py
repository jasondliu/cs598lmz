import io
# Test io.RawIOBase
# https://docs.python.org/3/library/io.html
class RawIOBase(io.RawIOBase):
    def __init__(self, source):
        self.source = source
        self.offset = 0
        self.name = source.name
        self.mode = source.mode
        self.closed = False
        self.buffer = b''
        self._buffer_size = 10
    def _fill_buffer(self, size=-1):
        if size == -1:
            data = self.source.read(self._buffer_size)
        else:
            data = self.source.read(size)
        if not data:
            return b''
        self.buffer += data
        return data
    def readable(self):
        return True
    def readinto(self, b):
        data = self._fill_buffer(len(b))
        n = len(data)
        b[:n] = data
        return n
    def read(self, n=None):
        if n is None:
            data = self.buffer
           
