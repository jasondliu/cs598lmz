import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r"):
        self.file = file
        self.mode = mode
        self.name = getattr(file, "name", None)
    def close(self):
        if self.closed:
            return
        try:
            if self.writable():
                self.flush()
        finally:
            self.closed = True
            try:
                file = self.detach()
            except Exception:
                pass
            else:
                if file is not None:
                    file.close()
    def __repr__(self):
        return "<{0.__class__.__name__} name={0.name!r} mode={0.mode!r}>".format(self)
    def fileno(self):
        return self.file.fileno()
    def seekable(self):
        return self.file.seekable()
    def readable(self):
        return self.mode in {"r", "r+", "a+"}
    def writable(self):
        return self.mode in {"w
