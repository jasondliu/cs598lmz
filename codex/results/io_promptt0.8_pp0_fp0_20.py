import io
# Test io.RawIOBase.readinto()
#class BytesIO(io.RawIOBase):
#    def __init__(self, initial_bytes=b''):
#        self._buf = initial_bytes
#        self._pos = 0
#
#    def readinto(self, b):
#        space = len(b)
#        n = space
#        if self._pos + space > len(self._buf):
#            n = len(self._buf) - self._pos
#        b[:n] = self._buf[self._pos:self._pos + n]
#        self._pos += n
#        return n
#
#    def write(self, b):
#        self._buf += b
#        self._pos = len(self._buf)
#
#    def flush(self):
#        pass
