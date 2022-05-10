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

# Issue #10338: check that the buffer is not freed before the
# BufferedReader is.

import weakref

class File(io.RawIOBase):
    def readinto(self, buf):
        pass
    def readable(self):
        return True

f = io.BufferedReader(File())
buf = f.read(1)
wr = weakref.ref(buf)
del buf
del f
assert wr() is not None

# Issue #10338: check that the buffer is freed when the BufferedReader
# is closed.

import weakref

class File(io.RawIOBase):
    def readinto(self, buf):
        pass
    def readable(self):
        return True

f = io.BufferedReader(File())
buf = f.read(1)
wr = weakref.ref(buf)
f.close()
del f
assert wr() is None

# Issue #10338: check that the buffer is freed when the BufferedReader
# is deleted.

import weakref

class File(io.RawIO
