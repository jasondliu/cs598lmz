import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='rb', closefd=True):
        self.filename = filename
        self.mode = mode
        self.closefd = closefd
        self.fd = None
        self.open(filename, mode, closefd)

    def open(self, filename, mode='rb', closefd=True):
        self.filename = filename
        self.mode = mode
        self.closefd = closefd
        self.fd = None
        if self.mode in ('w', 'wb'):
            self.fd = open(self.filename, self.mode)
        elif self.mode in ('r', 'rb'):
            self.fd = open(self.filename, self.mode)
        else:
            raise ValueError('invalid mode: %s' % self.mode)

    def close(self):
        if self.closefd:
            self.fd.close()

    def readable(self):
        return self.mode in ('r', 'rb')

    def writable(self):
        return self.mode in ('w', '
