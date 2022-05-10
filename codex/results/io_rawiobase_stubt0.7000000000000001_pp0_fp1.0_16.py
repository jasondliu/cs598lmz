import io
class File(io.RawIOBase):
    def __init__(self, file, mode="rb", closefd=True):
        self._file = file
        self._mode = mode
        self._closefd = closefd
        self._col = 0
        self._ln = 1
        self._pos = 0
        self._buf = b""
        self._buf_len = 0
        self._buf_pos = 0
        self._ch = None
        self._ch_pos = 0
        self._ch_g = False
        self._unget = False
    def read(self, n=None):
        if self._ch is not None and self._ch != b"":
            self._unget = True
            self._pos -= 1
            self._buf_pos -= 1
            self._col -= 1
        if n is None:
            return self._file.read()
        if n <= 0: return b""
        buf = b""
        for _ in range(n):
            ch = self.read1()
            if ch == b"":
                break
            buf += ch
        return buf
    def read
