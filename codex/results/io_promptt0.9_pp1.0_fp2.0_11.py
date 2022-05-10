import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    """Do-nothing Raw IO implementation."""
    def read(self, size=-1):
        return b''
    def readall(self):
        return b''
    def write(self, b):
        pass
    def seek(self, pos, whence=0):
        return 0
    def tell(self):
        return 0
    def truncate(self, pos=None):
        pass
    def close(self):
        pass
# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    """Do-nothing Buffered IO implementation."""
    def __init__(self):
        self.closed = False
    def close(self):
        pass
    @property
    def closed(self):
        return self._closed
    @closed.setter
    def closed(self, value):
        self._closed = value
# Test io.TextIOBase
class MyTextIO(io.TextIOBase):
    """Do-nothing Text IO implementation."""
    def __init__
