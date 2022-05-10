import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        
    def read(self, size=-1):
        if size == 0:
            return b''
        elif size < 0:
            return b'file content'
        else:
            return b'f' * size
        
    def write(self, b):
        return len(b)
    
    def seek(self, offset, whence=0):
        return 0
    
    def tell(self):
        return 0
    
    def close(self):
        pass
    
    def flush(self):
        pass
    
    def fileno(self):
        return -1
    
    def isatty(self):
        return False
    
    def readable(self):
        return 'r' in self.mode
    
    def writable(self):
        return 'w' in self.mode
    
    def seekable(self):
        return 'r' in self.mode
    
    def __repr__(self):
