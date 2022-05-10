import io
class File(io.RawIOBase):
    def __init__(self,  path, mode='r', encoding=None, errors=None, newline=None, closefd=True):
        self.raw = open(path, mode, closefd=True)
        
    def __del__(self):
        self.close()
        
    def read(self, n=-1):
        return self.raw.read(n)
    
    def readline(self, n=-1):
        return self.raw.readline(n)
    
    def readlines(self, hint=-1):
        return self.raw.readlines(hint)
    
    def write(self, b):
        return self.raw.write(b)
    
    def writelines(self, lines):
        return self.raw.writelines(lines)
    
    def seek(self, offset, whence=0):
        self.raw.seek(offset, whence)
        
    def tell(self):
        return self.raw.tell()
    
    def truncate(self, size=None):
        return self.raw
