import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        self.file.write(b)
        return len(b)
    def close(self):
        self.file.close()
    def flush(self):
        self.file.flush()
    def fileno(self):
        return self.file.fileno()
    def seekable(self):
        return self.file.seekable()
    def readable(self):
        return self.file.readable()
    def writable(self):
        return self.file.writable()
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def truncate(self, size=None):
        return self.file.truncate(size)
    def __iter__(self):
        return self.file.__iter__()
    def
