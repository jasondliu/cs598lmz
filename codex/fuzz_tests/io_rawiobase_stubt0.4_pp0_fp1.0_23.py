import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.open()
    def open(self):
        self.file = open(self.filename, self.mode)
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, data):
        return self.file.write(data)
    def seek(self, pos, whence=0):
        return self.file.seek(pos, whence)
    def tell(self):
        return self.file.tell()
    def isatty(self):
        return self.file.isatty()
    def flush(self):
        return self.file.flush()
    def readable(self):
        return self.file.readable()
    def writable(self):
        return self.file.writable()
    def seekable(self):
        return self.file.seekable()
    def
