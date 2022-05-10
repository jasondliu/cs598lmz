import io
class File(io.RawIOBase):
    def __init__(self, file_name, mode='r'):
        self.file_name = file_name
        self.mode = mode
    def read(self, size=None):
        with open(self.file_name, self.mode) as f:
            return f.read(size)
    def readline(self, size=-1):
        with open(self.file_name, self.mode) as f:
            return f.readline(size)
    def readlines(self, size=-1):
        with open(self.file_name, self.mode) as f:
            return f.readlines(size)
    def write(self, data):
        with open(self.file_name, self.mode) as f:
            return f.write(data)
    def writelines(self, data):
        with open(self.file_name, self.mode) as f:
            return f.writelines(data)
    def seek(self, offset, whence=io.SEEK_SET):
        with open(self.file_name
