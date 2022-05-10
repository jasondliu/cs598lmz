import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'x'*n
    def write(self, b):
        return len(b)
    def fileno(self):
        return 0
    def seekable(self):
        return True
    def seek(self, n, whence=0):
        return 0
    def tell(self):
        return 0
    def readable(self):
        return True
    def writable(self):
        return True
    def flush(self):
        return
    def close(self):
        return
# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def read(self, n=-1):
        return b'x'*n
    def write(self, b):
        return len(b)
    def flush(self):
        return
    def close(self):
        return
# Test io.TextIOBase
class MyTextIO(io.TextIOBase):
    def read(self, n=-1):
       
