import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        pass
    def write(self, b):
        pass
    def readable(self):
        return True
    def writable(self):
        return True

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def read(self, n=-1):
        pass
    def write(self, b):
        pass
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def seek(self, pos, whence=0):
        pass
    def tell(self):
        pass
    def truncate(self, pos=None):
        pass
    def detach(self):
        pass

# Test io.TextIOBase
class MyTextIO(io.TextIOBase):
    def read(self, n=-1):
        pass
    def write(self, b):
        pass
    def readable(self):
        return True
