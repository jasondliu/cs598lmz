import io
class File(io.RawIOBase):
    def __init__(self,f):
        self.f=f
        self.closed=False
    def close(self):
        if self.closed:
            raise ValueError("I/O operation on closed file")
    def fileno(self):
        self.f.fileno()
    def isatty(self):
        return self.f.isatty()
    def readable(self):
        return self.f.readable()
    def readline(self,size=-1):
        return self.f.readline(size)
    def seekable(self):
        return self.f.seekable()
    def writable(self):
        return self.f.writable()
    def readlines(self,sizehint=-1):
        return self.f.readlines(sizehint)
    def write(self,b):
        return self.f.write(b)
    def read(self,size=-1):
        return self.f.read(size)
    def write(self,b):
        return self.f.write(b)
