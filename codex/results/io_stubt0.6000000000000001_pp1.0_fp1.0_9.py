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

# Issue #17274: test weakrefs with __del__
class G:
    def __del__(self):
        pass

import weakref
gr = weakref.ref(G())
del gr

# Issue #17274: test weakrefs with __del__ and an exception
class H:
    def __del__(self):
        raise Exception

import weakref
hr = weakref.ref(H())
del hr

# Clear the C object cache, so that we can check that the
# freed objects are not in it.
import _testcapi
_testcapi.clear_c_object_cache()

# Issue #18091: test weakrefs with __del__ and reference cycles
# which trigger __del__ while the weakref is still alive.
import weakref

# A cycle that involves a list.
class I:
    def __init__(self):
        self.x = []
    def __del__(self):
        self.x.append(None)

i = I()
ir = weakref.ref(i)
del
