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
    def writeable(self):
        return True
    def write(self, b):
        self.file.write(b)
    def writelines(self, lines):
        self.file.writelines(lines)

class StringIO(io.StringIO):
    def __init__(self, buf=''):
        io.StringIO.__init__(self, buf)
    def getvalue(self):
        return io.StringIO.getvalue(self)

class BytesIO(io.BytesIO):
    def __init__(self, buf=b''):
        io.BytesIO.__init__(self, buf
