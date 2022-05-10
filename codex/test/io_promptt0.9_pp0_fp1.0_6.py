import io
# Test io.RawIOBase 
# https://docs.python.org/3/library/io.html#io.RawIOBase

# io.TextIOBase too, good to be ignored
class O(io.RawIOBase):
    def read(self):
        pass
    
    def readinto(self):
        pass
    
    def readable(self):
        pass
    
    def seek(self):
        pass
    
    def seekable(self):
        pass
    
    def tell(self):
        pass
    
    def truncate(self):
        pass
    
    def writeable(self):
        pass
    
    def writelines(self):
        pass
        
        
class S(io.StringIO):
    def read(self):
        pass
    
    def readinto(self):
        pass
    
    def readable(self):
        pass
    
    def seek(self):
        pass
    
    def seekable(self):
        pass
    
    def tell(self):
        pass
    
