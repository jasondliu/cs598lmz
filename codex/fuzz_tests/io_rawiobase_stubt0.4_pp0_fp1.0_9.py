import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r', closefd=True):
        self.file = file
        self.mode = mode
        self.closefd = closefd

    def read(self, size=-1):
        return self.file.read(size)

    def readinto(self, b):
        return self.file.readinto(b)

    def write(self, b):
        return self.file.write(b)

    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def close(self):
        if self.closefd:
            self.file.close()

class FileIO(io.RawIOBase):
    def __init__(self, file, mode='r', closefd=True):
        self.file = file
        self.mode = mode
        self.closefd = closefd

    def read(self, size=-1):
        return self.file.read(size)

    def readinto(self
