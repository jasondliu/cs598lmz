import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.fh = io.open(filename, mode)
        self.closed = False

    def close(self):
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        self.fh.close()
        self.closed = True

    def isatty(self):
        return False

    def readable(self):
        return 'r' in self.mode

    def writable(self):
        return 'w' in self.mode

    def seekable(self):
        return True

    def tell(self):
        return self.fh.tell()

    def write(self, b):
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        return self.fh.write(b)

    def read(self, n=-1):
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        return self.fh.read(n)
