import io
class File(io.RawIOBase):
    def __init__(self, fileobj):
        self.fileobj = fileobj
    def readinto(self, b):
        return self.fileobj.readinto(b)
    def write(self, b):
        return self.fileobj.write(b)
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return self.fileobj.seek(offset, whence)
    def tell(self):
        return self.fileobj.tell()
    def close(self):
        return self.fileobj.close()
    def __repr__(self):
        return repr(self.fileobj)
import sys
sys.modules[__name__] = File
