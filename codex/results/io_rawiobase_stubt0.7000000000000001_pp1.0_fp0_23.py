import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.fd = io.open(filename, mode)
        self.mode = mode
        self.closed = False
        self.softspace = 0
        self.encoding = None
        self.errors = None
        self.newlines = None
        self.line_buffering = False
        self.name = filename

    def close(self):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        self.closed = True
        self.fd.close()

    def fileno(self):
        return self.fd.fileno()

    def flush(self):
        self.fd.flush()

    def isatty(self):
        return self.fd.isatty()

    def readable(self):
        return "r" in self.mode

    def readline(self, size=-1):
        return self.fd.readline(size)

    def readlines(self, hint=-1):
        return self.fd.readlines(hint)

    def seek(
