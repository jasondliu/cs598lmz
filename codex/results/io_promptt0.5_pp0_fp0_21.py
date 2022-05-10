import io
# Test io.RawIOBase.  This is the base class for RawIOBase, BufferedIOBase
# and TextIOBase.

# Test that RawIOBase has the right attributes.
# Note that RawIOBase.readinto is not tested here.

# Note that there is no test for RawIOBase.readinto1() here, as it is an
# internal method.

class MyRawIOBase(io.RawIOBase):
    def __init__(self):
        self.readinto_called = False
        self.write_called = False
        self.seek_called = False
        self.tell_called = False
        self.close_called = False
        self.fileno_called = False

    def readinto(self, b):
        self.readinto_called = True
        return super().readinto(b)

    def readall(self):
        self.readall_called = True
        return super().readall()

    def readable(self):
        return True

    def write(self, b):
        self.write_called = True
        return super().write(b)

   
