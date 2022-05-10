import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def __init__(self):
        pass
        
    
    def readable(self):
        return True
    
    def read(self, n=-1):
        return "1"
        
    def writable(self):
        return True
        
    def write(self, b):
        return len(b)
        
    def readinto(self, b):
        b[:1] = [1]
        return 1
        
    def readall(self):
        return b""
        
    def seekable(self):
        return True
        
    def seek(self, pos, whence=0):
        pass
        
    def tell(self):
        return 0
        
    def truncate(self, pos=None):
        pass
        
    def read1(self, n):
        return b""
        
    def close(self):
        pass
        
raw = MyRawIO()
print(raw.readable())
print(raw.read())
print(raw.writable())

