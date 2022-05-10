import io
# Test io.RawIOBase.readinto(), which is only available in Python 3.

from io import RawIOBase

class MustNotBeCalled(Exception):
    pass

class TestRawIOBase(RawIOBase):
    def readable(self):
        return True

    def readinto(self, b):
        raise MustNotBeCalled


class TestRawIOBase2(RawIOBase):
    def readable(self):
        return True

    def readinto(self, b):
        return 0

class TestRawIOBase3(RawIOBase):
    def readable(self):
        return True

    def readinto(self, b):
        return b.__len__()

class TestRawIOBase4(RawIOBase):
    def readable(self):
        return True

    def readinto(self, b):
        self.readinto_called = True
        return b.__len__()

class TestRawIOBase5(RawIOBase):
    def readable(self):
        return True

    def readinto(self, b):
        b[:5] = b'abcde
