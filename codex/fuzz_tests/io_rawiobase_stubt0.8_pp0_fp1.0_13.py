import io
class File(io.RawIOBase):
    def __init__(self, deps=None):
        super().__init__()
        self.deps = deps
        self.pos = 0
        self.closed = False
    def fileno(self):
        return -1
    def flush(self):
        if self.closed:
            raise ValueError("flush of closed file")
    def isatty(self):
        if self.closed:
            raise ValueError("isatty of closed file")
        return False
    def readable(self):
        if self.closed:
            raise ValueError("readable of closed file")
        return True
    def readline(self, size=-1):
        if self.closed:
            raise ValueError("readline of closed file")
        n = size
        if n < 0:
            n = 99999
        i = self.pos
        while i < len(self.deps) and self.deps[i] != b"\n" and n > 1:
            i += 1
            n -= 1
        self.pos = i + 1
        return self.
