import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.file = open(filename, mode)
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, buf):
        return self.file.write(buf)
    def close(self):
        return self.file.close()
    def fileno(self):
        return self.file.fileno()
    def isatty(self):
        return self.file.isatty()
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def truncate(self, size=None):
        return self.file.truncate(size)
    def flush(self):
        return self.file.flush()
    def readable(self):
        return self.file.readable()
    def writable(self):
        return self.file.writable()
    def seekable(self):
        return self.file.seekable()
