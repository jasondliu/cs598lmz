import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, size=-1):
        return b'\x00'*size
    def write(self, b):
        return len(b)
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return True
    def seek(self, offset, whence=0):
        return 0
    def tell(self):
        return 0
    def close(self):
        return
    def flush(self):
        return

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw
    def read(self, size=-1):
        return b'\x00'*size
    def write(self, b):
        return len(b)
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return True
    def seek(self,
