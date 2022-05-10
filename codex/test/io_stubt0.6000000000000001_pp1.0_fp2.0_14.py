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

# Issue #10126: Test that objects with a destructor are not finalized
# before their __del__ method runs.
class Spam(object):
    def __del__(self):
        self.ran = True

import weakref
s = Spam()
r = weakref.ref(s)
del s
