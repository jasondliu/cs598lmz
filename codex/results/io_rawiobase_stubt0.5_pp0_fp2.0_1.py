import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r"):
        self.file = file
        self.mode = mode
        self.name = getattr(file, "name", None)
        self.closed = False
        self.softspace = 0
        self.newlines = None

    def close(self):
        if self.closed:
            return
        self.closed = True
        if hasattr(self.file, "close"):
            self.file.close()

    def fileno(self):
        return self.file.fileno()

    def isatty(self):
        return self.file.isatty()

    def flush(self):
        return self.file.flush()

    def seek(self, pos, whence=0):
        return self.file.seek(pos, whence)

    def tell(self):
        return self.file.tell()

    def truncate(self, pos=None):
        return self.file.truncate(pos)

    def write(self, b):
        return self.file.write(b)
