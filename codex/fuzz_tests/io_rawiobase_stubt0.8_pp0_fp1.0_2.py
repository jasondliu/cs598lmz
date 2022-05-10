import io
class File(io.RawIOBase):
    """Wraps a file descriptor."""

    def __init__(self, fd):
        self.fd = fd

    def close(self):
        try:
            return os.close(self.fd)
        finally:
            self.fd = None
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def fileno(self):
        return self.fd

    def isatty(self):
        return False

    def readable(self):
        return True

    def readinto(self, b):
        return os.read(self.fd, b)

    def readline(self, limit=-1):
        return io.BufferedIOBase.readline(self, limit)

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        return os.lseek(self.fd, offset, whence)

    def tell(self):
        return os.lseek(self.fd, 0,
