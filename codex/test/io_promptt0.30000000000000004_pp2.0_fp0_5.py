import io
# Test io.RawIOBase
class RawIOBaseSubclass(io.RawIOBase):
    def readable(self):
        return True
    def readinto(self, b):
        return 0
    def write(self, b):
        return 0

# Test io.BufferedIOBase
class BufferedIOBaseSubclass(io.BufferedIOBase):
    def readable(self):
        return True
    def readinto(self, b):
        return 0
    def write(self, b):
        return 0
    def seek(self, pos, whence=0):
        return 0
    def tell(self):
        return 0
    def truncate(self, pos=None):
        return 0

# Test io.TextIOBase
class TextIOBaseSubclass(io.TextIOBase):
    def readable(self):
        return True
    def readinto(self, b):
        return 0
    def write(self, b):
        return 0
    def seek(self, pos, whence=0):
        return 0
    def tell(self):
        return 0
