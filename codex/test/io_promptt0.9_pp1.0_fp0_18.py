import io
# Test io.RawIOBase subclassing

class MyRawIO(io.RawIOBase):
    def __init__(self, size):
        self.len = 7

    def readinto(self, b):
        pass

    def write(self, b):
        pass

    def seek(self, pos, whence):
        pass

    def readall(self):
        pass

    def close(self):
        pass

# Test that BufferedIOBase raises an error
try:
    class MyBufferedIO(io.BufferedIOBase):
        def __init__(self, size):
            self.len = 7

        def readinto(self, b):
            pass

        def write(self, b):
            pass

        def seek(self, pos, whence):
            pass
except TypeError:
    pass

# Test that StreamIOBase raises an error
