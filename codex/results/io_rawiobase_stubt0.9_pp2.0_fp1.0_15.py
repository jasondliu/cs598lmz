import io
class File(io.RawIOBase):
    def __init__(self,typ,name,*args,**kwargs):
        super(File,self).__init__()
        self._fp=open(name,typ,*args,**kwargs)
        self._off=0
        self._max=0
    def __len__(self):
        self._fp.seek(0,2)
        v=self._fp.tell()
        self._fp.seek(self._off,0)
        return v
    def close(self):
        self._fp.close()
    def seekable(self):
        return self._fp.seekable()
    def tell(self):
        return self._off
    def seek(self,offset,whence=0):
        if whence==0:
            self._fp.seek(offset,io.SEEK_SET)
        elif whence==1:
            self._fp.seek(offset,io.SEEK_CUR)
        elif whence==2:
            self._fp.seek(offset,2)
        self._off=self._fp.tell()
