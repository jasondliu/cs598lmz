import io
class File(io.RawIOBase):
    def __init__(self):
        self.pos=0
    def close(self):
        print('close')
        pass
    def fileno(self):
        pass
    def seek(self, off, whence=0):
        if whence==0:
            self.pos=off
        elif whence==1:
            self.pos+=off
        elif whence==2:
            self.pos=99+off
        return self.pos
    def seekable(self):
        return True
    def tell(self):
        return self.pos
    def read(self, size=-1):
        return 'hello'
    def readinto(self, b):
        pass
    def read1(self, size=-1):
        pass
    def readable(self)->bool:
        return True
    def flush(self)->None:
        pass
    def isatty(self):
        pass
    def readall(self)->bytes:
        pass
    def readline(self, limit=-1)->bytes:
        pass
    def readlines(self
