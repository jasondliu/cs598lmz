import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.fp = None

    def close(self):
        if self.fp is not None:
            self.fp.close()
        return True

    def fileno(self):
        if self.fp is None:
            self.fp = open(self.filename, self.mode)
        return self.fp.fileno()

    def flush(self):
        return True

    def isatty(self):
        return False

    def readable(self):
        return 'r' in self.mode

    def readline(self, size=-1):
        if self.fp is None:
            self.fp = open(self.filename, self.mode)
        return self.fp.readline(size)

    def readlines(self, hint=-1):
        if self.fp is None:
            self.fp = open(self.filename, self.mode)
        return self.fp.readlines(hint)

    def seek(self, offset, whence
