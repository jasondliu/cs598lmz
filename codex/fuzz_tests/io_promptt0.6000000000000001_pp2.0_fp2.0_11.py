import io
# Test io.RawIOBase
class FileIO(io.RawIOBase):
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return True
    def tell(self):
        return 42
    def seek(self, offset, whence):
        pass
    def readinto(self, b):
        return 5
    def write(self, b):
        pass
    def fileno(self):
        return 3
    def close(self):
        pass
print(FileIO())

# Test TextIOBase
class TextIO(io.TextIOBase):
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return True
    def tell(self):
        return 42
    def seek(self, offset, whence):
        pass
    def readinto(self, b):
        return 5
    def write(self, b):
        pass
    def fileno(self):
        return 3
    def close(self):
        pass
print(Text
