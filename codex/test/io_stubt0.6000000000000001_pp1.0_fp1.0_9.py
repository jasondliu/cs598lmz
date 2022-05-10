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
