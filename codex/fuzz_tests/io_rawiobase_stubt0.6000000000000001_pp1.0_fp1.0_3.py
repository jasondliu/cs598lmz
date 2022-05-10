import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read()
    def readable(self):
        return True

class LazyFile(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read()
    def readable(self):
        return True

class LazyFile2(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read()
    def readable(self):
        return True
    def readinto(self, b):
        data = self.file.read(len(b))
        b[:len(data)] = data
        return len(data)

class LazyFile3(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n
