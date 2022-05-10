import io
# Test io.RawIOBase
# See https://docs.python.org/3/library/io.html#io.RawIOBase
# for documentation on the RawIOBase class and its methods.

class MyRawIO(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.offset = 0
        
    def readable(self):
        return True
    
    def read(self, n=-1):
        if self.offset >= len(self.data):
            return ""
        if n < 0:
            n = len(self.data)
        result = self.data[self.offset:self.offset + n]
        self.offset += n
        return result
    
    def readall(self):
        return self.read()
    
    def readinto(self, b):
        n = len(b)
        result = self.read(n)
        b[:len(result)] = result
        return len(result)
    
    def seek(self, offset, whence=0):
        if whence == 0:
            self
