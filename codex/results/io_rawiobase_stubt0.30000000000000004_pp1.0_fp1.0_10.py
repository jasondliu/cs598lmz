import io
class File(io.RawIOBase):
    def __init__(self, file_path, mode='r'):
        self.file_path = file_path
        self.mode = mode
        self.file = None
        self.open()
        self.seek(0)
    def open(self):
        self.file = open(self.file_path, self.mode)
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)
    def readall(self):
        return self.file.readall()
    def readinto(self, b):
        return self.file.readinto(b)
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def write(self, b):
        return self.file.write(b)
    def writelines(self, lines):
        return self.file.writelines(lines)
    def __enter__(self):
        return self
