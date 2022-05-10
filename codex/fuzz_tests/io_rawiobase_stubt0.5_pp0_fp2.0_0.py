import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b'\x00' * n
    def seekable(self):
        return True
    def readable(self):
        return True
    def writeable(self):
        return False
    def seek(self, offset, whence=0):
        return 0
    def tell(self):
        return 0
    def writable(self):
        return False

class BytesIO(io.BytesIO):
    def write(self, b):
        pass
    def writable(self):
        return False

class StringIO(io.StringIO):
    def write(self, s):
        pass
    def writable(self):
        return False

class TextIOWrapper(io.TextIOWrapper):
    def write(self, s):
        pass
    def writable(self):
        return False

class BufferedWriter(io.BufferedWriter):
    def write(self, b):
        pass
    def writable(self):
        return False

class BufferedRWPair(io
