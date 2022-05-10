import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

import sys

sys.stdout = io.TextIOWrapper(io.BufferedWriter(f))
print(1)
del sys.stdout

import sys
sys.stdout = io.TextIOWrapper(io.BufferedWriter(f))
print(1)
del f
sys.stdout

# issue11644

import io
import sys

class Null():
    def write(self, data):
        pass

sys.stderr = Null()

# issue9923

import io

class MyRawIO(io.RawIOBase):
    def readinto(self, buffer):
        return len(buffer)

class MyBufferedIO(io.BufferedIOBase):
    def readinto(self, buffer):
        return len(buffer)

class MyTextIO(io.TextIOBase):
    def readinto(self, buffer):
        return len(buffer)

import io

class MyRawIO(io.RawIOBase):
    def writable(self):
        return True

    def write(self,
