import io
# Test io.RawIOBase readinto() return value, when read 0 bytes
# (see https://bugs.python.org/issue25573) and readinto(b"")


class ClassWithReadinto(io.RawIOBase):

    def readinto(self, b):
        return 0


