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
        return self.file.write(b)
    def writable(self):
        return True
    def writelines(self, lines):
        self.file.writelines(lines)
    def __getattr__(self, name):
        return getattr(self.file, name)

class StringIO(io.StringIO):
    def __init__(self, buf=''):
        io.StringIO.__init__(self, buf)
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()

def StringIO
