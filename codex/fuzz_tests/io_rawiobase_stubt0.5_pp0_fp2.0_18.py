import io
class File(io.RawIOBase):
    def __init__(self, filename, mode, *args, **kwargs):
        self.filename = filename
        self.mode = mode
        self.f = io.open(filename, mode, *args, **kwargs)
        self.f.__enter__()
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()
    def close(self):
        if self.f:
            self.f.__exit__(*sys.exc_info())
            self.f = None
    def __del__(self):
        self.close()
    def readable(self):
        return self.mode.startswith('r')
    def writable(self):
        return self.mode.startswith('w')
    def seekable(self):
        return True
    def fileno(self):
        return self.f.fileno()
    def seek(self, offset, whence=io.SEEK_SET):
        return self.f.seek(offset, whence)
    def tell(self
