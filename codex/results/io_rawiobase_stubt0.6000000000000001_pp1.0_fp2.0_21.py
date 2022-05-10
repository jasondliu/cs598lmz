import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r", closefd=True):
        self.file = file
        self.mode = mode
        self.closefd = closefd
        self.closed = False
        self.encoding = None
        self.newlines = None
        self.line_buffering = False

    def readable(self):
        return self.mode in ("r", "r+")

    def writable(self):
        return self.mode in ("w", "r+")

    def seekable(self):
        return True

    def close(self):
        if not self.closed:
            self.closed = True
            if self.closefd:
                self.file.close()

    def fileno(self):
        return self.file.fileno()

    def flush(self):
        pass

    def isatty(self):
        return self.file.isatty()

    def read(self, size=-1):
        return self.file.read(size)

    def readinto(self, b):
        return self.file.
