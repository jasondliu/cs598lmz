import io
class File(io.RawIOBase):
    def __init__(self, buffer=None):
        if buffer:
            self._buff = buffer
        else:
            self._buff = b''
        self._pos = 0
    def write(self, b):
        self._buff += b
        return len(b)
    def readinto(self, b):
        n = min(len(self._buff) - self._pos, len(b))
        if n == 0: return 0
        b[:n] = self._buff[self._pos:self._pos + n]
        self._pos += n
        return n
    def seek(self, n):
        if 0 <= n <= len(self._buff):
            self._pos = n
            return
        raise ValueError('seek out of range')
    def close(self):
        self._buff = b''
    def tell(self):
        return self._pos
    def fileno(self):
        return self._pos
    def seekable(self): return True
    def readable(self): return True
    def writable(self): return True
   
