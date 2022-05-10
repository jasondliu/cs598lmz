import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.file = open(filename, mode)
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, b):
        return self.file.write(b)
    def close(self):
        return self.file.close()

class File2(io.BufferedIOBase):
    def __init__(self, filename, mode):
        self.file = open(filename, mode)
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, b):
        return self.file.write(b)
    def close(self):
        return self.file.close()

class File3(io.TextIOBase):
    def __init__(self, filename, mode):
        self.file = open(filename, mode)
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, b):
        return self.file.write(
