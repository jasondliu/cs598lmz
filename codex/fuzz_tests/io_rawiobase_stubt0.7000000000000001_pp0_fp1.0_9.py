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

    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)

class InMemoryFile(File):
    def __init__(self, buf):
        self.buffer = io.BytesIO(buf)

class FileInData(File):
    def __init__(self, path, data):
        self.path = path
        self.data = data
        self.file = io.BytesIO(self.data)
        self.pos = 0
        self.closed = False

    def read(self, n=-1):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        self.pos = self.file.tell()
       s = self.file.read(n)
        return s

    def seekable
