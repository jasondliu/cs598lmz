import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r'):
        self.path = path
        self.mode = mode
        self.fd = os.open(path, os.O_RDONLY)
        if 'b' not in mode:
            self.fd = io.TextIOWrapper(self, encoding='utf-8')

    def read(self, size=-1):
        return os.read(self.fd, size)

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=os.SEEK_SET):
        return os.lseek(self.fd, offset, whence)

    def tell(self):
        return os.lseek(self.fd, 0, os.SEEK_CUR)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self.fd is not None:
            os.close(
