import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.file = io.FileIO(filename, mode)
        self.mode = mode
        self.encoding = None
        self.newlines = None
        self.closed = False

    def close(self):
        self.file.close()
        self.closed = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def flush(self):
        self.file.flush()

    def fileno(self):
        return self.file.fileno()

    def isatty(self):
        return self.file.isatty()

    def readable(self):
        return self.mode in ('r', 'r+', 'a+')

    def readline(self, size=-1):
        return self.file.readline(size)

    def readlines(self, hint=-1):
        return self.file.readlines(hint)

    def seek(
