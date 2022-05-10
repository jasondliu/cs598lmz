import io
class File(io.RawIOBase):
    def __init__(self, name, mode, buffering=-1):
        self.closed = False
        self.mode = mode
        self.name = name
        self.buffering = buffering

    def close(self):
        self.closed = True

    def fileno(self, *args, **kwargs):
        return self.name

    def seek(self, offset, whence=0):
        raise io.UnsupportedOperation

    def getvalue(self):
        return self.name

class TextIO(File):
    def read(self, n=-1):
        return self.name

    def write(self, s):
        self.name = s

class BinaryIO(File):
    def read(self, n=-1):
        return self.name

    def write(self, s):
        self.name = s
