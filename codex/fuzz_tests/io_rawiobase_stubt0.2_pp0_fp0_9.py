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
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def write(self, b):
        self.file.write(b)
    def writable(self):
        return True
    def writelines(self, lines):
        self.file.writelines(lines)
    def __next__(self):
        return self.file.__next__()
    def __iter__(self):
        return self.file.__iter__()
    def close(self):
        self.file.close()
    def flush(self):
        self.file.flush()
    def isatty(self):
        return self.file.isatty()
    def read1(self, n):
