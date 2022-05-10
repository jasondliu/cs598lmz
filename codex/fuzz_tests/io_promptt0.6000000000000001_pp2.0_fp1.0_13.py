import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):

    def read(self, n=-1):
        return b"\x00" * n

    def write(self, b):
        return len(b)

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):

    def read(self, n=-1):
        return b"\x00" * n

    def write(self, b):
        return len(b)

# Test io.TextIOBase
class MyTextIO(io.TextIOBase):

    def read(self, n=-1):
        return "0" * n

    def write(self, s):
        return len(s)

# Test io.FileIO
class MyFileIO(io.FileIO):
    pass

# Test io.BytesIO
class MyBytesIO(io.BytesIO):
    pass

# Test io.StringIO
class MyStringIO(io.StringIO):
    pass

# Test io.BufferedReader
class MyBufferedReader(io.BufferedReader
