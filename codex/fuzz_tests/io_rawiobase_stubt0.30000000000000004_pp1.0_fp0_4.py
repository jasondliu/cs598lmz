import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = None
    def open(self):
        self.file = open(self.name, 'rb')
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def readinto(self, b):
        return self.file.readinto(b)
    def __repr__(self):
        return '<%s %r>' % (self.__class__.__name__, self.name)

class CachedFile(File):
    def __init__(self, name):
        super().__init__(name)
        self.cache = b''
    def readinto(self, b):
        if self.cache:
            n = len(b)
            output, self.cache = self.cache[:n], self.cache[n:]
            b[:len(output)] = output
            return len(output)
        return self.file.readinto(b)
    def read(self,
