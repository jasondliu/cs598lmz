import io
# Test io.RawIOBase

io.RawIOBase.readinto()
io.RawIOBase.readinto1()

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        raise NotImplementedError

class MyRawIO(io.RawIOBase):
    def readinto1(self, b):
        raise NotImplementedError

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        b[:] = b'a' * len(b)
        return len(b)

    def readinto1(self, b):
        b[:] = b'a' * len(b)
        return len(b)

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        b[:] = b'a' * len(b)
        return len(b)

    def readinto1(self, b):
        b[:] = b'a' * len(b)
        return len(b)

class MyRawIO(io.RawIOBase):

