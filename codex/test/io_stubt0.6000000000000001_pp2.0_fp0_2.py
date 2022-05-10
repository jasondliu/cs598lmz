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

import _io

class File(_io.FileIO):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = _io.BufferedReader(File(0))
f.read(1)
del f

# Issue #18698: Test that the garbage collector doesn't crash when it
# collects a BufferedReader whose underlying file object has a
# non-NULL weakreflist.

# The test only passes if the underlying file object's weakreflist
# contains a dead reference.  So, we create a weakref to the file
# object, let it die, and then create the BufferedReader.

import weakref

class File(io.RawIOBase):
    def readinto(self, buf):
        pass
    def readable(self):
        return True

f = File()
w = weakref.ref(f)
del f
f = io.BufferedReader(File())
del w
del f

