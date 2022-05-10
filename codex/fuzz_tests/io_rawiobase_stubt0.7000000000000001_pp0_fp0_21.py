import io
class File(io.RawIOBase):
    def __init__(self, path, mode, *args, **kwargs):
        io.RawIOBase.__init__(self)
        self.mode = mode
        if 'r' in mode:
            self.mode = 'r'
        elif 'w' in mode or 'a' in mode:
            self.mode = 'w'
        self.fp = iolib.open(path, self.mode)

    def __del__(self):
        self.close()

    def close(self):
        if self.fp is not None:
            self.fp.close()
            self.fp = None

    def readable(self):
        return 'r' in self.mode

    def writable(self):
        return 'w' in self.mode

    def seekable(self):
        return True

    def readinto(self, b):
        data = self.fp.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if
