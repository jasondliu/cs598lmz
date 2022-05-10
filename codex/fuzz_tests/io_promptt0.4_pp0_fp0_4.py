import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'\x00' * n

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def read(self, n=-1):
        return b'\x00' * n

# Test io.TextIOBase
class MyTextIO(io.TextIOBase):
    def read(self, n=-1):
        return '\x00' * n

# Test io.BytesIO
class MyBytesIO(io.BytesIO):
    def read(self, n=-1):
        return b'\x00' * n

# Test io.StringIO
class MyStringIO(io.StringIO):
    def read(self, n=-1):
        return '\x00' * n

# Test io.FileIO
class MyFileIO(io.FileIO):
    def read(self, n=-1):
        return b'\x00' * n

# Test io.BufferedReader
class
