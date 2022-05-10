import io
class File(io.RawIOBase):
    def __init__(self, path):
        if os.path.isfile(path) != True:
            raise ValueError('Invalid argument')
        self.file = open(path,'rb')
    def tell(self):      
        return self.file.tell()
    def seek(self,offset,whence=0):
        self.file.seek(offset,whence)
        return self.tell()
    def isatty(self):
        return False
    def fileno(self):
        return self.file.fileno()
    def close(self):
        self.file.close()
    def readable(self):
        return self.file.readable()
    def writable(self):
        return self.file.writable()
    def seekable(self):
        return self.file.seekable()
    def readinto(self,b):
        if hasattr(b, "tobytes"):
            return self.file.readinto(b)
        else:
            return self.readinto(memoryview(b))
    def read(self,
