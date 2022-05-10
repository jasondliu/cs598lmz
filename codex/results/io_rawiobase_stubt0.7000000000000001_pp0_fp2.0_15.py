import io
class File(io.RawIOBase):
    
    def __init__(self, path):
        self.path = path
        self.file = None
        
    def open(self):
        self.file = open(self.path, 'rb')
        
    def close(self):
        self.file.close()
        
    def __enter__(self):
        self.open()
        return self
    
    def __exit__(self, *args):
        self.close()
        
    def readable(self):
        return True
    
    def readinto(self, b):
        return self.file.readinto(b)
    
    def writeable(self):
        return True
    
    def write(self, b):
        return self.file.write(b)
    
    def seekable(self):
        return True
    
    def seek(self, pos, whence=0):
        return self.file.seek(pos, whence)
    
    def tell(self):
        return self.file.tell()
    
    
    
    
    
    
    
