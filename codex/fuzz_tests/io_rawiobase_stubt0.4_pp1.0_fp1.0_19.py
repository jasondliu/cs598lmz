import io
class File(io.RawIOBase):
    def __init__(self, filename, mode="r"):
        self.file = open(filename, mode)
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, b):
        return self.file.write(b)
    def close(self):
        return self.file.close()

# This is the class that will be used to create the file object.
# It will be passed to the constructor of the class that will
# actually read the data.
class FileReader(object):
    def __init__(self, filename, mode="r"):
        self.file = File(filename, mode)
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def write(self, b):
        return self.file.write(
