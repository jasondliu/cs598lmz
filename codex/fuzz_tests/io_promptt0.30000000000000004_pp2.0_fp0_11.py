import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'x' * n
    def write(self, b):
        pass
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return True
    def seek(self, offset, whence=0):
        pass
    def tell(self):
        return 0
    def close(self):
        pass
    def flush(self):
        pass

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def read(self, n=-1):
        return b'x' * n
    def write(self, b):
        pass
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return True
    def seek(self, offset, whence=0):
        pass
    def tell(self):
        return 0
    def close(self):
        pass

