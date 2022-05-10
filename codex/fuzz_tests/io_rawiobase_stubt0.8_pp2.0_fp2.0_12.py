import io
class File(io.RawIOBase):
    def __init__(self, filepath):
        self.filepath=filepath
        self.file=open(self.filepath,'rb')
    def readable(self):
        return True
    def seekable(self):
        return True
    def fileno(self):
        return self.file.fileno()
    def seek(self,pos):
        return self.file.seek(pos)
    def tell(self):
        return self.file.tell()
    def read(self, n):
        return self.file.read(n)
    def readinto(self, b):
        buf=self.file.read(len(b))
        n=len(buf)
        try:
            b[:n]=buf
        except TypeError as err:
            import array
            if not isinstance(b,array.array):
                raise err
            b[:n]=array.array('b',buf)
        return n

def is_gzip(file):
    if hasattr(file,"readinto1"):
        return False
    try:
