import io
# Test io.RawIOBase.readall()

class MyRawIO(io.RawIOBase):
    def readall(self):
        return b'abc'

class MyRawIO2(io.RawIOBase):
    def readall(self):
        return 'abc'

class MyRawIO3(io.RawIOBase):
    def readall(self):
        return u'abc'

class MyRawIO4(io.RawIOBase):
    def readall(self):
        return bytearray(b'abc')

class MyRawIO5(io.RawIOBase):
    def readall(self):
        return memoryview(b'abc')

class MyRawIO6(io.RawIOBase):
    def readall(self):
        return iter(b'abc')

class MyRawIO7(io.RawIOBase):
    def readall(self):
        return io.BytesIO(b'abc')

class MyRawIO8(io.RawIOBase):
    def readall(self):
        return io.StringIO('abc')

class
