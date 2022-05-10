import io
# Test io.RawIOBase

class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return 'foo'

    def write(self, b):
        return len(b)

class MyRawIO1(io.RawIOBase):
    def read(self, n=-1):
        return 'foo'

    def write(self, b):
        return len(b)

    def fileno(self):
        return -1

    def seekable(self):
        return False

    def readable(self):
        return True

    def writable(self):
        return False

    def seek(self, n, whence=0):
        raise io.UnsupportedOperation()

    def tell(self):
        raise io.UnsupportedOperation()

    def truncate(self, n=None):
        raise io.UnsupportedOperation()

class MyRawIO2(io.RawIOBase):
    def read(self, n=-1):
        return 'foo'

    def write(self, b):
        return len(b)

