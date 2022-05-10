import io
# Test io.RawIOBase
# Test io.RawIOBase.readinto()
# Test io.RawIOBase.readinto1()

# This test checks that io.RawIOBase.readinto() behaves
# according to the docs.

# Currently, the only RawIOBase classes defined in CPython are
# io.FileIO and io.BufferedRandom. FileIO, however, only
# supports reading, and BufferedRandom has a readinto()
# method, but it's not a RawIOBase method, so it's not
# tested here.

# Therefore, this test is just a smoke test.

# io.RawIOBase.readinto()

class MyRawIOBase(io.RawIOBase):
    def readinto(self, b):
        return super().readinto(b)


class MyRawIOBase2(io.RawIOBase):
    def readinto(self, b):
        return super().readinto(b)

    def readinto1(self, b):
        return super().readinto1(b)


