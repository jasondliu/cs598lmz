import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.fobj = None
        self.pos = 0
        self.closed = False
    def __enter__(self):
        self.fobj = open(self.name, self.mode)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    def close(self):
        if self.fobj is not None:
            self.fobj.close()
        self.closed = True
    def readable(self):
        return self.mode[0] in 'r+'
    def writable(self):
        return self.mode[0] in 'wa+'
    def seekable(self):
        return True
    def seek(self, pos, whence=0):
        if self.fobj is None:
            self.fobj = open(self.name, self.mode)
        self.fobj.seek(pos, whence)
        self.pos = self
