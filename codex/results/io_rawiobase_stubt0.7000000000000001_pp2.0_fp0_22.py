import io
class File(io.RawIOBase):
    """
    Wrapper which handles 'close' and 'name' for a raw file object.
    """
    def __init__(self, name, mode, closefd=True):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.file = io.open(name, mode, closefd=closefd)

    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None

    def __del__(self):
        self.close()

    def __repr__(self):
        f = self.file
        if f is None:
            return '<%s [closed]>' % self.__class__.__name__
        return repr(f)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def __getattr__(self, attr):
        return getattr(self.file, attr)

    def __iter__(self):
        return iter
