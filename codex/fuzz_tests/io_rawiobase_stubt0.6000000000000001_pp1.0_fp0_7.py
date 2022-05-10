import io
class File(io.RawIOBase):
    def __init__(self,name):
        self.name=name
        self.f=open(name,mode='rb')
    def read(self,size=-1):
        return self.f.read(size)
    def seek(self,offset,whence=0):
        return self.f.seek(offset,whence)
    def __del__(self):
        self.f.close()
def open(name):
    return File(name)
f=open('/tmp/test/hello.txt')
f.read()

#简化上面的代码
import io
class File(io.RawIOBase):
    def __init__(self,name):
        self.name=name
        self.f=open(name,mode='rb')
    def __getattr__(self, attr):
        return getattr(self.f,attr)
    def __del__(self):
        self.f.close()
def open(name):
    return File(name)
f=open('/tmp/
