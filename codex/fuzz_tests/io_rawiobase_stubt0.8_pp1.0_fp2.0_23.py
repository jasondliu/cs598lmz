import io
class File(io.RawIOBase):
    def __init__(self,filepath):
        self.filepath=filepath
        self.fp=open(self.filepath,'rb')
        self.byteorder=config.byteorder
        if self.fp.readline().strip()!='#!STDIN':
            raise BadSigError("File signature does not match.")
    def close(self):
        self.fp.close()
    def readable(self):
        return True
    def readinto(self,buffer):
        data=self.fp.read(len(buffer))
        if data:
            buffer[:len(data)]=data
        return len(data)
    def read(self,n=-1):
        return self.fp.read(n)
    def readall(self):
        return self.fp.read()
    def readline(self,n=-1):
        return self.fp.readline(n)
