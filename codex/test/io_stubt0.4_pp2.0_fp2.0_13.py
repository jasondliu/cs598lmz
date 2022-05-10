import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

# Issue #10

class MyIO(io.IOBase):
    def close(self):
        pass

class MyRawIO(io.RawIOBase):
    def close(self):
        pass

class MyBufferedIO(io.BufferedIOBase):
    def close(self):
        pass

class MyBytesIO(io.BytesIO):
    def close(self):
        pass

class MyStringIO(io.StringIO):
    def close(self):
        pass

class MyTextIO(io.TextIOBase):
    def close(self):
        pass

# Issue #11

class MyRawIO(io.RawIOBase):
    def readinto1(self, buf):
        pass

# Issue #12

class MyRawIO(io.RawIOBase):
    def readinto1(self, buf):
        pass

# Issue #13

class MyRawIO(io.RawIOBase):
    def readinto1(self, buf):
        pass

# Issue #14

