import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r', closefd=True):
        self.name = filename
        self.mode = mode
        self.closefd = closefd
        self.fd = os.open(filename, mode)
        self.is_open = True
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()
    def close(self):
        if self.closefd:
            os.close(self.fd)
        self.is_open = False
    def readable(self):
        return self.mode in ('r', 'r+', 'a+')
    def writable(self):
        return self.mode in ('w', 'w+', 'a', 'a+')
    def seekable(self):
        return True
    def seek(self, offset, whence=os.SEEK_SET):
        return os.lseek(self.fd, offset, whence)
    def fileno(self):
        return self.fd

