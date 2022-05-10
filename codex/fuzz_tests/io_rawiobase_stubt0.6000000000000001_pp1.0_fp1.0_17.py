import io
class File(io.RawIOBase):
    def __init__(self, filename, mode="r"):
        self.file = io.open(filename, mode)
        self.size = os.stat(filename).st_size
    def readable(self):
        return True
    def readinto(self, b):
        if len(b) == 0:
            return 0
        return self.file.readinto(b)
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def __sizeof__(self):
        return self.size

# For the sake of simplicity, we use the same file for both reading
# and writing.
with File(__file__, mode="r+") as f:
    print(f.tell())
    print(f.read(10))
    f.seek(5)
    print(f.tell())
    print(f.read(10))
    f.seek(5)
