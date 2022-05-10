import io
# Test io.RawIOBase.readinto() method

import _io

class CIoSubclass(io.RawIOBase):
    def readinto(self, b):
        return super().readinto(b)

class PyIoSubclass(io.RawIOBase):
    def readinto(self, b):
        return super().readinto(b)

class CReadintoSubclass(CIoSubclass):
    def readinto(self, b):
        return super().readinto(b)

class PyReadintoSubclass(PyIoSubclass):
    def readinto(self, b)
