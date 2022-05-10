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

# This is a test for a bug in the garbage collector.  The bug was that
# the gc didn't call tp_clear() on objects that had their own
# allocation.  This was fixed by making the gc traverse the objects
# in the arena in which they were allocated.

import gc

class X(object):
    def __del__(self):
        pass

gc.collect()

# This is a test for a bug in the garbage collector.  The bug was that
# the gc didn't call tp_clear() on objects that had their own
# allocation.  This was fixed by making the gc traverse the objects
# in the arena in which they were allocated.

import gc

class X(object):
    def __del__(self):
        pass

gc.collect()

# This is a test for a bug in the garbage collector.  The bug was that
# the gc didn't call tp_clear() on objects that had their own
# allocation.  This was fixed by making the gc traverse the objects
# in the arena in which they
