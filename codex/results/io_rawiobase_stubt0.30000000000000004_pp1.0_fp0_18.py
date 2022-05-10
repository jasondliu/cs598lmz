import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        return self.file.write(b)
    def close(self):
        return self.file.close()
    def flush(self):
        return self.file.flush()
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
    def fileno(self):
        return self.file.fileno()
    def isatty(self):
        return self.file.isatty()
    def __enter__(self):
        return self.file.__enter__()
    def __exit__(self, *args):
