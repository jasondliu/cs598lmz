import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def write(self, b):
        return self.file.write(b)
    def writable(self):
        return True
    def writelines(self, lines):
        return self.file.writelines(lines)
    def __next__(self):
        return next(self.file)
    def __iter__(self):
        return self
    def close(self):
        return self.file.close()
    def flush(self):
        return self.file.flush()
    def fileno(self):
        return self.file.fileno()
    def isatty(self):
        return self.file.
