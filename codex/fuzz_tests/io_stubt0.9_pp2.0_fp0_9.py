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

import gc; gc.collect()
assert view is None

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

import gc; gc.collect()
assert view is None

class File(io.RawIOBase):
    def read(self, n):
        return b"\0" * n
    def readable(self):
        return True

f = io.BufferedReader(File())
assert f.read(1) == b"\0"
del f

import gc; gc.collect()
assert view is None

class File(io.RawIOBase):
    def read(self, n):
        return b"\0" * n
    def readable(self):
        return True

f = io.BufferedReader(File())
assert f.read(1) == b"\0"
del f

import g
