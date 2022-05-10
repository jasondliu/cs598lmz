import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r', closefd=True):
        self._file = file
        self._closefd = closefd
        self._opened = False
        opening = getattr(file, "opening", None)
        if opening is not None:
            opening(self)
        self._opened = True
        io.IOBase.__init__(self)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return False

    def readinto(self, b):
        return self._file.readinto(b)

    def readall(self):
        return self._file.readall()

    @property
    def name(self):
        return self._file.name

    @property
    def mode(self):
        return self._file.mode

    def fileno(self):
        return self._file.fileno()

    def
