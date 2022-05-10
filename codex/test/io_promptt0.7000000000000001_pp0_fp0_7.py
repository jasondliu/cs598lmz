import io
# Test io.RawIOBase interface
class RawStream(io.RawIOBase):
    def read(self, n=-1):
        return b'x'*n
    
    def write(self, b):
        return len(b)
    
    def seekable(self):
        return True
    
    def seek(self, n, whence=0):
        return 0
    
    def tell(self):
        return 0
    
    def flush(self):
        return 0
    
    def read1(self, n):
        return b'x'*n
    
    def close(self):
        pass
s = RawStream()
s.read(0)

s.read(1)

s.read(10)

s.read()

s.read1(5)

