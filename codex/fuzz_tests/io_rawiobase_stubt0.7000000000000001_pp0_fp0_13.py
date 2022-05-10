import io
class File(io.RawIOBase):
    def __init__(self,name):
        self.f = open(name,'rb',0)
        super().__init__()
    def close(self):
        return self.f.close()
    def read(self,n):
        return self.f.read(n)
    def seek(self,n):
        return self.f.seek(n)
    def tell(self):
        return self.f.tell()
    def fileno(self):
        return self.f.fileno()
    def isatty(self):
        return self.f.isatty()
    def readable(self):
        return self.f.readable()
    def seekable(self):
        return self.f.seekable()
    def writable(self):
        return self.f.writable()

_read = File.read
_seek = File.seek
_tell = File.tell

class StringIO(io.StringIO):
    def close(self):
        return self.getvalue()

_StringIO = StringIO

class Bytes
