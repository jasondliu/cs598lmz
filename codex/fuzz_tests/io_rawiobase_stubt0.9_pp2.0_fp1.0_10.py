import io
class File(io.RawIOBase):
    def __init__(self,filename):
        super().__init__()
        self.f = open(filename,"rb")
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return False
    
    def close(self):
        self.f.close()
        
    def readinto(self,b):
        with open(self.f.name,"rb") as f:
            data = f.read(1*1024*1024)
            if len(data) == 0:
                return 0
            b[:len(data)] = data
            return len(data)
    
    def tell(self):
        return self.f.tell()
    
    def seek(self,offset, whence=io.SEEK_SET):
        return self.f.seek(offset,whence)
 

fname = "wget.exe" 
base = File(fname)

elf = ELFFile(base)
elf.stream.seek(elf.elfclass)
classname
