import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'abc'

class MyRawIO2(io.RawIOBase):
    def read(self, n=-1):
        return b'abc'
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def tell(self):
        return 0
    def close(self):
        pass

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def read(self, n=-1):
        return b'abc'

class MyBufferedIO2(io.BufferedIOBase):
    def read(self, n=-1):
        return b'abc'
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def tell(self):
        return 0
    def close(self):
        pass

# Test io
