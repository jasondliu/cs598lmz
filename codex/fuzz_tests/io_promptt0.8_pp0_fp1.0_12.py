import io
# Test io.RawIOBase.readinto()
from io import RawIOBase
from random import randint
from random import shuffle
from itertools import chain
from functools import partial
from test import support

class B1(RawIOBase):
    def readinto(self, b):
        return 0

class B2(RawIOBase):
    def readinto(self, b):
        return len(b)

class B3(RawIOBase):
    def readable(self):
        return True
    def readinto(self, b):
        return 0

class B4(B3):
    def readinto(self, b):
        return len(b)

class C1(RawIOBase):
    def readinto(self, b):
        for i in range(len(b)):
            b[i] = 0
        return len(b)

class C2(RawIOBase):
    def readinto(self, b):
        return b.__len__()

class C3(RawIOBase):
    def readable(self):
        return True
    def readinto
