import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        if mode not in ('r', 'w'):
            raise ValueError('invalid mode')
        self.name = name
        self.mode = mode

    def read(self, size=-1):
        if self.mode != 'r':
            raise IOError('not open for reading')
        return os.read(self.fd, size)

    def write(self, b):
        if self.mode != 'w':
            raise IOError('not open for writing')
        return os.write(self.fd, b)

    def seek(self, offset, whence=os.SEEK_SET):
        return os.lseek(self.fd, offset, whence)

    def fileno(self):
        return self.fd

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def tell(self):
        return os.lseek(self.fd, 0, os.SEEK_CUR)

    def flush(self):
