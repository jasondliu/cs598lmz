import io
class File(io.RawIOBase):
    def __init__(self, fch):
        self.fch = fch
    def close(self):
        self.fch.close()
    def fileno(self):
        return self.fch.fileno()
    def isatty(self):
        return False
    def read(self, n=-1):
        return self.fch.read(n)
    def readable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        self.fch.seek(offset, whence)
    def seekable(self):
        return True
    def tell(self):
        return self.fch.tell()
    def write(self, b):
        return self.fch.write(b)
    def writable(self):
        return True

def open(fname, mode="rt", fch=None, **kwargs):
    if fch is None:
        fch = io.open(fname, mode=mode, **kwargs)
    return File(fch)

class
