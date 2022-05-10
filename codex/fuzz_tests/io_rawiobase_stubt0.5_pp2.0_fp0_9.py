import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
        self.buf = bytearray(8192)
        self.buf_pos = 0
        self.buf_end = 0
        self.buf_len = 8192
        self.closed = False
        self.mode = 'rb'
        self.name = f.name
        self.newlines = None
        self.softspace = 0

    def _read(self, n):
        """Read and return at most n bytes.

        If the call was unsuccessful, raise an IOError.
        """
        if n < 0:
            raise IOError("Can't read from file")
        if n == 0:
            return b''
        if self.buf_pos == self.buf_end:
            self._fill_buffer()
        if self.buf_pos == self.buf_end:
            return b''
        if n > self.buf_end - self.buf_pos:
            n = self.buf_end - self.buf_pos
        assert n > 0
        res = self.
