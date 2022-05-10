import io
# Test io.RawIOBase
# Test io.BufferedIOBase
# Test io.BufferedIOBase.readinto
# Test io.BufferedIOBase.readinto1

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        b[:3] = b'foo'
        return 3

class MyBufferedIO(io.BufferedIOBase):
    def readinto(self, b):
        b[:3] = b'foo'
        return 3

class MyBufferedReader(io.BufferedReader):
    def readinto(self, b):
        b[:3] = b'foo'
        return 3

class MyBufferedWriter(io.BufferedWriter):
    def write(self, b):
        if not b.startswith(b'foo'):
            raise ValueError
        return len(b)

class MyBufferedRandom(io.BufferedRandom):
    def readinto(self, b):
        b[:3] = b'foo'
        return 3
    def write(self, b):
       
