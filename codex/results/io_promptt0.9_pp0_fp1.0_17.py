import io
# Test io.RawIOBase, io.BufferedIOBase, io.TextIOBase

# A lot of this testing is trying to exercise the abstract methods defined
# by the base class.  We do that with a simple no-op implementation defined
# in this file.
# (If any of them are not defined, you'll get a TypeError from the abstract
# method checker in the base class definition.  The C and C++ implementations
# of the base classes are not protected by the same checker for performance
# reasons.)

class NoOpIO(io.RawIOBase):
    def readinto(self, b):
        if b:
            b[0] = ord('A')
            return 1
        return 0

    def write(self, b):
        pass

class NoOpBufferedIO(io.BufferedIOBase):
    def read(self, n=-1):
        return b'B'

class NoOpTextIO(io.TextIOBase):
    def read(self, n=-1):
        return 'C'

class TestRawIOBase:
    def test_nonzero(self):

