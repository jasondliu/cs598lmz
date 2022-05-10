import io
class File(io.RawIOBase):
    def __init__(self):
        self.offset = 0
        
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset += offset
        elif whence == io.SEEK_END:
            self.offset = len(self.data) + offset
        return self.offset
    
    def tell(self):
        return self.offset
    
    def read(self, n=-1):
        if n >= 0:
            self.offset += n
            return self.data[self.offset-n:self.offset]
        else:
            return self.data[self.offset:]
    
    def readall(self):
        return self.data[self.offset:]
    
    def readinto(self, b):
        data = self.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err
