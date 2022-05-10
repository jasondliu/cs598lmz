import io
# Test io.RawIOBase
import io

class RawIOTest(io.RawIOBase):

    def readable(self):
        return True

    def readinto(self, b):
        n = len(b)
        b[:] = [42] * n
        return n

# Test io.BufferedIOBase
import io

class BufferedIOTest(io.BufferedIOBase):

    def readable(self):
        return True

    def readinto(self, b):
        n = len(b)
        b[:] = [42] * n
        return n

# Test io.TextIOBase
import io

class TextIOTest(io.TextIOBase):

    def readable(self):
        return True

    def read(self, n):
        return "a" * n

# Test io.FileIO
import io

class FileIOTest(io.FileIO):

    def readable(self):
        return True

    def readinto(self, b):
        n = len(b)
        b[:] = [42] * n
        return
