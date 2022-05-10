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
# the gc didn't call tp_clear() on objects that had a destructor
# (tp_dealloc) but didn't have a tp_clear.

import gc

class C:
    def __del__(self):
        pass

gc.collect()

# This is a test for a bug in the garbage collector.  The bug was that
# the gc didn't call tp_clear() on objects that had a destructor
# (tp_dealloc) but didn't have a tp_clear.

import gc

class C:
    def __del__(self):
        pass

gc.collect()

# This is a test for a bug in the garbage collector.  The bug was that
# the gc didn't call tp_clear() on objects that had a destructor
# (tp_dealloc) but didn't have a tp_clear.

import gc

class C:
    def __del__(self):
        pass

gc
