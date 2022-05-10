import io
# Test io.RawIOBase
# Test io.BufferedIOBase
# Test io.TextIOBase

class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'abc'
    def write(self, b):
        pass
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return True
    def seek(self, n, whence=0):
        pass
    def tell(self):
        return 0
    def close(self):
        pass

class MyBufferedIO(io.BufferedIOBase):
    def read(self, n=-1):
        return b'abc'
    def write(self, b):
        pass
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return True
    def seek(self, n, whence=0):
        pass
    def tell(self):
        return 0
    def close(self):
        pass

class MyTextIO
