import io
class File(io.RawIOBase):
    def read(self, length):
        return b''
f=File()
print(f,f.read)
print(io.RawIOBase.read.__self__)

class MyClass(object):
    def __init__(self,t):
        self.t=t
    
l=MyClass(4)
print(MyClass.__bases__)
print(l.__class__)
