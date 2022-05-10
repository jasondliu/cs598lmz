import io
# Test io.RawIOBase, which is an abstract class
# as of Python 3.5.
class AnIO(io.RawIOBase):
    def read(self, size):
        return None
    def write(self, data):
        return None

AnIO().write(b"a")

class AnIO(io.RawIOBase):
    def read(self, size):
        return None
    def write(self, data):
        return None
    def seek(self, offset, whence=io.SEEK_SET):
        return None

AnIO().write(b"a")

class AnIO(io.RawIOBase):
    def read(self, size):
        return None
    def write(self, data):
        return None
    def seek(self, offset, whence=io.SEEK_SET):
        return None
    def seekable(self):
        return True

AnIO().write(b"a")

class AnIO(io.RawIOBase):
    def read(self, size):
        return None
    def write(self, data):
        return None
