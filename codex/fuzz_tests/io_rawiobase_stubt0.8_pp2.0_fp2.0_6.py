import io
class File(io.RawIOBase):
    def __init__(self,path):
        self.p=Path(path)
        self.f=self.p.open("r+")
    def seek(self,offset,whence=0):
        if whence == 0:
            self.f.seek(offset)
        elif whence == 1:
            self.f.seek(self.f.tell()+offset)
        elif whence == 2:
            self.f.seek(self.p.stat().st_size+offset)
        else:
            raise ValueError("invalid whence ({}, should be 0, 1 or 2)".format(whence))
    def tell(self):
        return self.f.tell()
    def truncate(self, size=None):
        if size is None:
            self.f.truncate()
        else:
            self.f.truncate(size)
    def read(self,n=-1):
        return bytearray(self.f.read(n))
    def write(self,b):
        self.f.write(b)
