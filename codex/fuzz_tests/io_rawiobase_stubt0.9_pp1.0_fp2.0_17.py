import io
class File(io.RawIOBase):
    """my file class"""
    
    def writable(self):
        """是否可写"""
        
        return False
    
    def readable(self):
        """是否可读"""
        
        return False
    
    def seekable(self):
        """是否可移动"""
        
        return True
f = File()
f.writable()

f.readable()
f.seekable()

class FileReader(io.RawIOBase):
    def __init__(self, filename, mode="rb"):
        self._pos = 0
        self._fp = open(filename, mode=mode)
    
    def readable(self):
        return True
        
    def readinto(self, b):
        size = len(b)
        ret = self._fp.read(size)
        
        self._pos += len(ret)
        return len(ret)
r = FileReader("../files/create.py")
r.readinto(bytearray(8))
data = r
