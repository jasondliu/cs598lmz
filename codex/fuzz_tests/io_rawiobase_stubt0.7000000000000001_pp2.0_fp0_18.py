import io
class File(io.RawIOBase):
    def write(self):
        pass
    def writelines(self):
        pass
    def read(self):
        pass
    def readinto(self):
        pass
    def readline(self):
        pass
    def flush(self):
        pass
    def isatty(self):
        pass
    def readall(self):
        pass
    def __enter__(self):
        pass
    def __exit__(self):
        pass
    def tell(self):
        pass
    def seek(self,offset,whence):
        pass

class TextIOWrapper(TextIOBase):
    def __init__(self,buffer,encoding,errors,newline,line_buffering):
        pass
    def read(self,size):
        pass
    def readline(self,limit=-1):
        pass
    def readlines(self,hint=-1):
        pass
    def write(self,s):
        pass
    def writelines(self,lines):
        pass
    def __enter__(self):
        pass

