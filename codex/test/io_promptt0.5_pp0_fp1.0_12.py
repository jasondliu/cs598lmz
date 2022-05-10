import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'x' * n
    def write(self, b):
        pass
    def seek(self, offset, whence=io.SEEK_SET):
        pass
    def seekable(self):
        return True

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def read(self, n=-1):
        return b'x' * n
    def write(self, b):
        pass
    def seek(self, offset, whence=io.SEEK_SET):
        pass
    def seekable(self):
        return True

# Test io.TextIOBase
class MyTextIO(io.TextIOBase):
    def read(self, n=-1):
        return 'x' * n
    def write(self, b):
        pass
    def seek(self, offset, whence=io.SEEK_SET):
        pass
    def seekable(self):
        return True

# Test
