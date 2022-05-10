import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
        return len(b)
    def close(self):
        return self.f.close()
    def fileno(self):
        return self.f.fileno()
    def flush(self):
        return self.f.flush()
    def isatty(self):
        return self.f.isatty()
    def readable(self):
        return self.f.readable()
    def seekable(self):
        return self.f.seekable()
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def writable(self):
        return self.f.writable()
    def writelines(self, lines):
        self.f.writelines(lines)

class FileWra
