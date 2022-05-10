import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def write(self, b):
        self.file.write(b)
    def writable(self):
        return True
    def flush(self):
        self.file.flush()

#---------------------------------------------------------------------------------------------------

class Stream(io.RawIOBase):
    def __init__(self, stream):
        self.stream = stream
    def read(self, n=-1):
        return self.stream.read(n)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self.stream.seek(offset, whence)

