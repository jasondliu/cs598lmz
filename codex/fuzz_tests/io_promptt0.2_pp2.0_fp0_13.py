import io
# Test io.RawIOBase

import _io

class MyRawIO(_io.RawIOBase):
    def readinto(self, b):
        b[:] = b'\x00'*len(b)
        return len(b)

class MyRawIO2(_io.RawIOBase):
    def readinto(self, b):
        b[:] = b'\x00'*len(b)
        return len(b)
    def readall(self):
        return b'\x00'*100

class MyRawIO3(_io.RawIOBase):
    def readinto(self, b):
        b[:] = b'\x00'*len(b)
        return len(b)
    def readall(self):
        return b'\x00'*100
    def readable(self):
        return True

class MyRawIO4(_io.RawIOBase):
    def readinto(self, b):
        b[:] = b'\x00'*len(b)
        return len(b)
    def readall(self):
       
