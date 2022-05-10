import io
# Test io.RawIOBase.readinto()

import _io

def readinto_helper(b, n):
    b[0] = ord('x')
    return n

class ReadintoRawIO(_io.RawIOBase):
    def readinto(self, b):
        return readinto_helper(b, len(b))

class ReadintoBufferedIO(_io.BufferedIOBase):
    def readinto(self, b):
        return readinto_helper(b, len(b))

class ReadintoBytesIO(io.BytesIO):
    def readinto(self, b):
        return readinto_helper(b, len(b))

class ReadintoStringIO(io.StringIO):
    def readinto(self, b):
        return readinto_helper(b, len(b))

class ReadintoIOBase(io.IOBase):
    def readinto(self, b):
        return readinto_helper(b, len(b))

class ReadintoFileIO(io.FileIO):
    def readinto(self, b):

