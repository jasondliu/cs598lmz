import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.len = os.fstat(file.fileno()).st_size
        self.pos = 0
        self.buf = ''
    def read(self, n=-1):
        if n >= 0:
            end = self.pos + n
            if end > self.len:
                end = self.len
        else:
            if self.pos >= self.len:
                return ''
            end = self.len
        while len(self.buf) < end - self.pos:
            chunk = self.file.read(min(16384, end - self.pos - len(self.buf)))
            if not chunk:
                raise EOFError
            self.buf += chunk
        res = self.buf[:end - self.pos]
        self.buf = self.buf[len(res):]
        self.pos = end
        return res
    def read1(self, n):
        return self.read(n)
    def seekable(self):
        return True

