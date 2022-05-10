import io
class File(io.RawIOBase):
    def __init__(self,filename):
        super().__init__()
        self.file = ""
        self.file = os.open(filename,os.O_RDWR)
        self.curpos = 0

    def tell(self):
        return self.curpos

    def seek(self,pos,flag=0):
        if flag == io.SEEK_SET or flag == 0:
            if(pos < 0 or pos > os.path.getsize(self.file)):
                return 0
            else:
                self.curpos = pos
        elif flag == io.SEEK_END:
            if(pos + os.path.getsize(self.file) < 0):
                return 0
            else:
                self.curpos = os.path.getsize(self.file) + pos
        else:
            self.curpos +=pos

    def read(self,size=-1):
        if size > 0:
            ret = os.read(self.file,size)
            self.curpos += len(ret)
            return ret
       
