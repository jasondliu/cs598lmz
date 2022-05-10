import io
# Test io.RawIOBase
import io
import _io

class MyRawIO(_io.RawIOBase):
    def read(self, n=-1):
        return b"a"*n

    def write(self, b):
        return len(b)

    def seekable(self):
        return False

class MyRawIO2(_io.RawIOBase):
    def read(self, n=-1):
        return b"a"*n

    def write(self, b):
        return len(b)

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        pass

    def tell(self):
        return 0

class MyRawIO3(_io.RawIOBase):
    def read(self, n=-1):
        return b"a"*n

    def write(self, b):
        return len(b)

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        pass

    def tell(self):
        return 0

    def close(self):
       
