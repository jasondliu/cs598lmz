import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return 'abc'

    def write(self, b):
        return 1

    def readable(self):
        return True

    def writable(self):
        return True

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def read(self, n=-1):
        return 'abc'

    def write(self, b):
        return 1

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        return 100

    def tell(self):
        return 200

    def truncate(self):
        return 300

    def readinto(self, b):
        return 0

    def read1(self, n):
        return 'abc'

    def detach(self):
        return 1

# Test io.TextIOBase
