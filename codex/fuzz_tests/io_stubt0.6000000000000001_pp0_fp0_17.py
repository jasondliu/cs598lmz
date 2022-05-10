import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

def read(self, n=-1):
    if n is None:
        n = -1
    elif n is not None and n < 0:
        raise ValueError("negative count")
    if n is -1:
        n = sys.maxsize
    if self._blksize <= 1:
        new_pos = max(0, self._pos - self._buf_len + 1)
    else:
        new_pos = self._pos
    if new_pos < 0:
        raise ValueError("seek() before start of file")
    if n == 0:
        return b""
    new_pos += n
    if new_pos - self._pos > self._buf_len:
        self._seek(new_pos)
        self._read_block()
    new_pos = min(new_pos, self._pos + self._buf_len)
    r = self._buf[self._pos:new_pos]
    self._pos = new_pos
    return r

def read1(self, n):
    buf = bytearray(n
