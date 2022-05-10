import io
class File(io.RawIOBase):
    def read(self,n=-1):
        ...
    def readinto(self,b):
        ...
    def readline(self,length=None):
        ...
    def write(self,b):
        ...
#快捷方式
#import io
class File(io.RawIOBase):
    def read(self,n=-1):
        ...
    def readinto(self,b):
        ...
    def readline(self,length=None):
        ...
    def write(self,b):
        ...
#基于内存的操作
import array
class FileLike(io.RawIOBase):
    def readinto(self,b):
        n = len(b)
        try:
            b[:n] = self.data[self.offset:self.offset+n]
            self.offset += n
            return n
        except IndexError:
            self.offset = len(self.data)
            return 0
import array
class FileLike(io.RawIOBase):
    def
