import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, size=-1):
        return self.f.read()
    def readable(self):
        return True
    def seekable(self):
        return False
    def close(self):
        self.f.close()

#-------------------------------------------------------------------------------

class Reader:
    def __init__(self, reader):
        self.reader = reader
    def read(self, size=-1):
        return self.reader.Read(size)
    def seekable(self):
        return False
    def close(self):
        pass

#-------------------------------------------------------------------------------

class Stream:
    def __init__(self, stream):
        self.stream = stream
    def read(self, size=-1):
        b = self.stream.Read(size)
        return b.ToArray()
    def seekable(self):
        return False
    def close(self):
        pass

#-------------------------------------------------------------------------------

class IStream(io.RawIOBase):
    def __init__(self, stream
