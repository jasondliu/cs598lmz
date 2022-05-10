import io
class File(io.RawIOBase):
    """
    Wrapper for the file object.
    """
    def __init__(self, file):
        self.file = file
        self.mode = file.mode

    def readable(self):
        return True

    def writeable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        return self.file.readinto(b)

    def read(self, n=-1):
        return self.file.read(n)

    def write(self, b):
        return self.file.write(b)

    def seek(self, n):
        return self.file.seek(n)

    def tell(self):
        return self.file.tell()

class FileReader(io.FileIO):
    """
    Wrapper for the file object.
    """
    def __init__(self, file):
        self.file = file
        self.mode = file.mode

    def readable(self):
        return True

    def writeable(self):
        return True

    def
