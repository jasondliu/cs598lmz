import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return super().read(n)
    
    def readinto(self, b):
        return super().readinto(b)
    
    def write(self, b):
        return super().write(b)
    
    def seek(self, offset, whence=0):
        return super().seek(offset, whence)
    
    def tell(self):
        return super().tell()
    
    def truncate(self, size=None):
        return super().truncate(size)
    
    def detach(self):
        return super().detach()
    
    def fileno(self):
        return super().fileno()
    
    def seekable(self):
        return super().seekable()
    
    def readable(self):
        return super().readable()
    
    def writable(self):
        return super().writable()
    
    def readline(self, limit=-1):
        return super().readline(limit)
    
    def readlines(self, hint=-1):
       
