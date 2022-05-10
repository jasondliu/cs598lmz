import io
# Test io.RawIOBase
class RawIO(io.RawIOBase):
    def read(self, n=-1):
        pass
    def write(self, b):
        pass
    def seek(self, offset, whence=0):
        pass
    def tell(self):
        pass
    def close(self):
        pass

# Test io.BufferedIOBase
class BufferedIO(io.BufferedIOBase):
    def read(self, n=-1):
        pass
    def write(self, b):
        pass
    def seek(self, offset, whence=0):
        pass
    def tell(self):
        pass
    def close(self):
        pass

# Test io.TextIOBase
class TextIO(io.TextIOBase):
    def read(self, n=-1):
        pass
    def write(self, b):
        pass
    def seek(self, offset, whence=0):
        pass
    def tell(self):
        pass
    def close(self):
        pass

# Test io.FileIO
