import io
class File(io.RawIOBase):
    def readable(self):
        return True

    def writeable(self):
        return True

    def seekable(self):
        return True

    def __init__(self, filepath):
        self.data = open(filepath,'rb').read()
        self.wseek=0
        self.filepath=filepath


    def read(self,size=None):
        if self.wseek>len(self.data):
            ret='\0'*size
        else:
            if size is None or size+self.wseek>=len(self.data):
                ret=self.data[self.wseek:]
            else:
                ret=self.data[self.wseek:self.wseek+size]
                self.wseek+=size
        return ret

    def readinto(self,b):
        if self.wseek>len(self.data):
            ret=0
        else:
            if len(b)==0:
                ret=0
            else:
                b[:]=self.data[self.wseek:self
