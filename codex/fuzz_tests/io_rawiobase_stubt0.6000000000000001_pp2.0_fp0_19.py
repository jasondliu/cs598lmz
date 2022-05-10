import io
class File(io.RawIOBase):

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self._is_closed = False
        self._file = builtins.open(filename, mode)

    def close(self):
        if self._is_closed:
            return
        self._is_closed = True
        self._file.close()

    def readable(self):
        return self.mode == "r"

    def writable(self):
        return self.mode == "w"

    def seekable(self):
        return False

    def readinto(self, b):
        return self._file.readinto(b)

    def write(self, b):
        return self._file.write(b)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()


def open(filename, mode="r"):
    return File(filename, mode)
