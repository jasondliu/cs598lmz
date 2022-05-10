import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r"):
        self.file = file
        self.mode = mode
        self.name = getattr(file, "name", None)
        self.closed = False

    def close(self):
        if self.closed:
            return
        self.closed = True
        self.file.close()

    def fileno(self):
        self.file.fileno()

    def isatty(self):
        return self.file.isatty()

    def readable(self):
        return "r" in self.mode

    def writable(self):
        return "w" in self.mode

    def seekable(self):
        return True

    def readinto(self, b):
        data = self.file.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array(b
