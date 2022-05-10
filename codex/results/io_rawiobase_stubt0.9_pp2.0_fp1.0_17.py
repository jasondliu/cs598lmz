import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b'a litlle bit data'
 
    def seekable(self):
        return True
 
    def writable(self):
        return False
 
    def seek(self, offset, whence=io.SEEK_SET):
        return 0
 
    def tell(self):
        return 0
 
    def write(self, b):
        pass
 
f = File()
print(f.read())
print(f.read())
print(f.read())



#In [48]: f = File()
#
#In [49]: f.read()
#Out[49]: b'a litlle bit data'
#
#In [50]: f.read()
#Out[50]: b'a litlle bit data'
#
#In [51]: f.read()
#Out[51]: b'a litlle bit data'
