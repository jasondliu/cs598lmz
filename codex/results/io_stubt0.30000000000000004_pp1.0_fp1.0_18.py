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

# This is a test for issue #9074.
# The problem is that the __del__ method of BufferedReader
# calls the raw stream's close method, which in turn calls
# the raw stream's flush method.  If the raw stream's flush
# method is implemented in Python, it may trigger a recursive
# call to the raw stream's readinto method, which in turn
# may trigger a recursive call to the raw stream's close
# method.  The fix is to prevent the raw stream's close
# method from being called.

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

# This is a test for issue #9074.
# The problem is that the __del__ method of BufferedReader
# calls the raw stream's close method, which in turn calls
# the raw stream's flush method.  If the raw stream's flush
# method is implemented in Python
