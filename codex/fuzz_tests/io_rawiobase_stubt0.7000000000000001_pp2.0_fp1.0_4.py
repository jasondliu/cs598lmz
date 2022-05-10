import io
class File(io.RawIOBase):
    def __init__(self,size):
        self.size=size
        self.chunk_size=1024
        self.count=self.size/self.chunk_size
        self.count=int(self.count)
        self.left=self.size-self.count*self.chunk_size
    def read(self,size):
        if(size == 0):
            return b''
        if(size>self.size):
            size=self.size
        if(size<=self.chunk_size):
            data=os.urandom(size)
            self.size-=size
            return data
        data=os.urandom(self.chunk_size)
        self.count-=1
        self.size-=self.chunk_size
        return data+self.read(size-self.chunk_size)
    
    def readable(self):
        return True
    
    def seekable(self):
        return True
    
    def seek(self,offset,whence=0):
        if(whence
