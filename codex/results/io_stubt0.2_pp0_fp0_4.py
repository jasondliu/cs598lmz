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

# This is a test for issue #12093.
# The following code should not crash.
import io
import os

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
f.close()
del f

# This is a test for issue #12093.
# The following code should not crash.
import io
import os

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
f.close()
f.close()
del f

# This is a test for issue #12093.
# The following code should not crash.
import io
import os

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
       
