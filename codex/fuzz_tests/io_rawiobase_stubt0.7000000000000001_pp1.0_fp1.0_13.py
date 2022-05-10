import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
    def isatty(self):
        return False
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return True
    def close(self):
        if self.closed:
            return
        self.closed = True
        try:
            self.flush()
        finally:
            if not self.fd.closed:
                self.fd.close()
    def __repr__(self):
        return repr(self.fd)
    def __del__(self):
        try:
            self.close()
        except (NameError, AttributeError):
            pass
    def closefd(self):
        self.fd.closefd()
    def fileno(self):
        return self.fd.fileno()
    def flush(self):
        self.fd.flush()
    def seek(self, pos, whence=0):
        self.fd.seek(pos, whence)
    def tell(
