import io
# Test io.RawIOBase

import _io

class MyRawIO(_io.RawIOBase):
    def read(self, n=-1):
        return b'x' * n
    def write(self, b):
        return len(b)

class MyBufferedRawIO(_io.BufferedIOBase):
    def read(self, n=-1):
        return b'x' * n
    def write(self, b):
        return len(b)

class MyBufferedReader(_io.BufferedReader):
    def read(self, n=-1):
        return b'x' * n

class MyBufferedWriter(_io.BufferedWriter):
    def write(self, b):
        return len(b)

class MyBufferedRWPair(_io.BufferedRWPair):
    def read(self, n=-1):
        return b'x' * n
    def write(self, b):
        return len(b)

class MyBufferedRandom(_io.BufferedRandom):
    def read(self, n=-1):
        return b'x
