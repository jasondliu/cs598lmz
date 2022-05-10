import io
# Test io.RawIOBase

import _io

class MyRawIO(_io.RawIOBase):
    def readinto(self, b):
        b[:3] = b"foo"
        return 3

class MyRawIO2(_io.RawIOBase):
    def readinto(self, b):
        b[:3] = b"foo"
        return 3

    def readinto1(self, b):
        b[:3] = b"foo"
        return 3

class MyRawIO3(_io.RawIOBase):
    def readinto(self, b):
        b[:3] = b"foo"
        return 3

    def readinto1(self, b):
        b[:3] = b"foo"
        return 3

    def readinto2(self, b):
        b[:3] = b"foo"
        return 3

class MyRawIO4(_io.RawIOBase):
    def readinto(self, b):
        b[:3] = b"foo"
        return 3

    def readinto1(self, b
