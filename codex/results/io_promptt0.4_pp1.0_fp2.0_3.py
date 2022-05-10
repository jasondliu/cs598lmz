import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, size=-1):
        pass
    def write(self, b):
        pass
    def seekable(self):
        return False
    def readable(self):
        return True
    def writable(self):
        return True
    def fileno(self):
        return 42
    def close(self):
        pass
    def seek(self, offset, whence=0):
        pass
    def tell(self):
        pass
    def truncate(self, size=None):
        pass
    def readall(self):
        pass
    def readinto(self, b):
        pass
    def readinto1(self, b):
        pass
    def writeall(self, b):
        pass
    def detach(self):
        pass
    def read1(self, size=-1):
        pass
    def readline(self, size=-1):
        pass
    def readlines(self, hint=-1):
        pass
    def writelines(self, lines):
        pass
