import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r'):
        self.path = path
        self.mode = mode
        self.handle = None
    def open(self):
        self.handle = open(self.path, self.mode)
    def close(self):
        self.handle.close()
    def read(self, size=-1):
        return self.handle.read(size)
    def write(self, data):
        return self.handle.write(data)
    def seek(self, offset, whence=0):
        return self.handle.seek(offset, whence)
    def tell(self):
        return self.handle.tell()
    def flush(self):
        return self.handle.flush()
    def fileno(self):
        return self.handle.fileno()
    def isatty(self):
        return self.handle.isatty()
    def readable(self):
        return self.handle.readable()
    def writable(self):
        return self.handle.writable()
    def seekable(self):

