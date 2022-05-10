import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        # Find the right file.
        self.fp = open(filename, mode)
        # Create a file object to return.
        self.file = io.FileIO(self.fp.fileno(), mode)

    def read(self, n=-1): return self.file.read(n)
    def writelines(self, lines): return self.file.writelines(lines)
    def readline(self, limit=-1): return self.file.readline(limit)
    def readable(self): return self.file.readable()
    def writable(self): return self.file.writable()
    def seekable(self): return self.file.seekable()
    def write(self, data): return self.file.write(data)
    def tell(self): return self.file.tell()
    def flush(self): return self.file.flush()
    def seek(self, pos, whence=0): return self.file.seek(pos, whence)
    def close(self):
        r = self.file.
