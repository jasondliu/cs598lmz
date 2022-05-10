import io
# Test io.RawIOBase interface

class T(io.RawIOBase):
    def __init__(self):
        self.closed = 0
    def read(self,n):
        return 'x' * n
    def write(self,s):
        pass
    def close(self):
        self.closed = 1

