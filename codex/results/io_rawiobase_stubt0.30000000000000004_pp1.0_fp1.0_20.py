import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.mode = None
        self.encoding = None
        self.newlines = None
        self.softspace = 0
    def __enter__(self):
        self.file = open(self.filename, self.mode, self.buffering, self.encoding, self.errors, self.newlines)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
    def close(self):
        if self.file is not None:
            self.file.close()
        self.file = None
    def fileno(self):
        return self.file.fileno()
    def flush(self):
        self.file.flush()
    def isatty(self):
        return self.file.isatty()
    def readable(self):
        return self.file.readable()
    def readline(self, size=-1):
        return self.file.readline
