import io
class File(io.RawIOBase):
    def __init__(self, path, mode="r", bufsize=-1):
        self.path = path
        self.mode = mode
        self.bufsize = bufsize
        self.pos = 0
        self.closed = False
        self.name = path

    def close(self):
        self.closed = True

    def fileno(self):
        return -1

    def flush(self):
        pass

    def isatty(self):
        return False

    def readable(self):
        return "r" in self.mode

    def readline(self, size=-1):
        if not self.readable():
            raise io.UnsupportedOperation("not readable")
        with open(self.path, "r") as f:
            f.seek(self.pos)
            if size < 0:
                line = f.readline()
            else:
                line = f.readline(size)
            self.pos = f.tell()
        return line

    def readlines(self, hint=-1):
        if not self.readable():
            raise
