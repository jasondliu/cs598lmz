import io
class File(io.RawIOBase):
    def __init__(self,name):
        self.name=name
        self.pos=0
        self.length=0
        return
    def open(self,*args):
        self.pos=0
        self.length=0
        self.f=io.open(self.name,*args)
        return self
    def close(self):
        try:
            self.f.close()
        except Exception:
            pass
        return
    def flush(self):
        return self.f.flush()
    def read(self,n=-1):
        x=self.f.read(n)
        self.length+=-1 if n<0 else len(x)
        return x
    def readinto(self,x):
        y=self.f.readinto(x)
        self.length+=y
        return y
    def readline(self,n=-1):
        x=self.f.readline(n)
        self.length+=len(x)
        return x
    def readlines(self,n=-1):

