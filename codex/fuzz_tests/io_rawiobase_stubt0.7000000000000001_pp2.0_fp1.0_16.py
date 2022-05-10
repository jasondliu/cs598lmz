import io
class File(io.RawIOBase):
    def __init__(self,file_name):
        self.file_name = file_name
        self.fh = None
    def open(self):
        if self.fh is not None:
            raise IOError("File is already open")
        self.fh = io.open(self.file_name,mode='rb')
    def close(self):
        if self.fh is None:
            raise AttributeError("File is not open")
        self.fh.close()
        self.fh = None
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def readinto(self,b):
        if self.fh is None:
            raise AttributeError("File is not open")
        return self.fh.readinto(b)
    def read(self,n=-1):
        if self.fh is None:
            raise AttributeError("File is not open")
        return self.fh.read(n)
    def
