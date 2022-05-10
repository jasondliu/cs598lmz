import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self.file = file
        self.mode = mode

    def read(self, n=-1):
        return self.file.read(n)

    def write(self, b):
        self.file.write(b)
        return len(b)

    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None

    def flush(self):
        if 'w' in self.mode or 'a' in self.mode:
            self.file.flush()

    def fileno(self):
        return self.file.fileno()

    def isatty(self):
        return self.file.isatty()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_
