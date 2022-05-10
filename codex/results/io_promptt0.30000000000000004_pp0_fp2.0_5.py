import io
# Test io.RawIOBase
class RawI(io.RawIOBase):
    def read(self, n=-1):
        return b"abc"
    def write(self, b):
        pass
    def seek(self, n, whence=0):
        pass
    def tell(self):
        return 0
    def close(self):
        pass
    def fileno(self):
        return 0

# Test io.BufferedIOBase
class BufferedI(io.BufferedIOBase):
    def read(self, n=-1):
        return b"abc"
    def write(self, b):
        pass
    def seek(self, n, whence=0):
        pass
    def tell(self):
        return 0
    def close(self):
        pass
    def fileno(self):
        return 0

# Test io.TextIOBase
class TextI(io.TextIOBase):
    def read(self, n=-1):
        return "abc"
    def write(self, b):
        pass
    def seek(self, n, whence=0):

