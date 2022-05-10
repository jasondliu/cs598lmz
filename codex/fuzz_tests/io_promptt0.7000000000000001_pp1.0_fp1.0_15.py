import io
# Test io.RawIOBase 
# 继承 RawIOBase，可以实现自定义的文件类型
class RawIOTest(io.RawIOBase):
    def __init__(self):
        self.offset = 0
    
    def read(self, n=-1):
        if n < 0:
            return b''
        else:
            if self.offset == 0:
                self.offset += 1
                return b'p'
            elif self.offset == 1:
                self.offset += 1
                return b'y'
            elif self.offset == 2:
                self.offset += 1
                return b'\n'
            else:
                return b''
    
    def readable(self):
        return True
    
    def write(self, b):
        pass
    
    def writable(self):
        return True
    
    def seekable(self):
        return False
    
    def seek(self):
        pass
    
    def tell(self
