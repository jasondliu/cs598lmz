import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, size=None):
        raise NotImplementedError
    def readinto(self, b):
        raise NotImplementedError
    def write(self, b):
        raise NotImplementedError
# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def read(self, n=None):
        raise NotImplementedError
    def read1(self, n=None):
        raise NotImplementedError
    def write(self, b):
        raise NotImplementedError
    def flush(self):
        raise NotImplementedError
    def detach(self):
        raise NotImplementedError
# Test io.TextIOBase
class MyTextIO(io.TextIOBase):
    def read(self, n=None):
        raise NotImplementedError
    def readline(self, limit=-1):
        raise NotImplementedError
    def write(self, b):
        raise NotImplementedError
    def flush
