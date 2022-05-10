import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r', buffering=-1):
        self.file = io.FileIO(path, mode, buffering)
        self.mode = mode
        self.name = path
        self.encoding = None
        self.closed = False
        self.errors = None
        self.newlines = None
        self.line_buffering = False
        self.softspace = False

    def __repr__(self):
        return repr(self.file)

    def fileno(self):
        return self.file.fileno()

    def isatty(self):
        return self.file.isatty()

    def close(self):
        self.file.close()

    def flush(self):
        self.file.flush()

    def readable(self):
        return self.file.readable()

    def writable(self):
        return self.file.writable()

    def seekable(self):
        return self.file.seekable()

    def readinto(self, b):
        return self.file.
