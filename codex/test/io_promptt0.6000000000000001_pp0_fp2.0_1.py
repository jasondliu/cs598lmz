import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        pass

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def read(self, n=-1):
        pass

# Test io.TextIOBase
class MyTextIO(io.TextIOBase):
    def read(self, n=-1):
        pass

# Test io.BytesIO
class MyBytesIO(io.BytesIO):
    def read(self, n=-1):
        pass

# Test io.StringIO
class MyStringIO(io.StringIO):
    def read(self, n=-1):
        pass
