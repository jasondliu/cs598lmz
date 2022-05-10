import io
class File(io.RawIOBase):
    """
    # 继承io.RawIOBase
    """
    def __init__(self, name, mode='r', closefd=True):
        if not closefd:
            raise NotImplementedError()
        if isinstance(name, str):
            self.name = name
            self.closefd = closefd
            self.mode = mode
            super().__init__()
        else:
            self.f = name
            self.name = self.f.name
            self.mode = self.f.mode
            self.closefd = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __iter__(self):
        with self as f:
            yield from f

    def readable(self):
        return 'r' in self.mode

    def writable(self):
        return 'w' in self.mode

    def seekable(self):
        return True

    def close(self):
        if self.
