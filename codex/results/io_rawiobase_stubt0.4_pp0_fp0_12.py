import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = None
        self.pos = 0
        self.closed = False

    def __repr__(self):
        return f'<File {self.name}>'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self.file:
            self.file.close()
        self.closed = True

    def fileno(self):
        return self.file.fileno()

    def flush(self):
        self.file.flush()

    def isatty(self):
        return self.file.isatty()

    def readable(self):
        return self.mode == 'r'

    def readline(self, limit=-1):
        return self.file.readline(limit)

    def readlines(self, hint=-1):
        return self.file.read
