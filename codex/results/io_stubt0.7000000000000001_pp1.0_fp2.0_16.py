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
print(view)
"""

"""
import io

class File(io.RawIOBase):
    closed = 0
    def __del__(self):
        self.closed = 1
    def fileno(self):
        return 1
    def close(self):
        self.closed = 2

f = File()
print(f.closed)
f.close()
print(f.closed)
del f
print(f.closed)
"""

"""
import io

class BackwardsReader(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = BackwardsReader()
f.read(1)
del f
print(view)
"""

"""
import io

class BackwardsReader(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(BackwardsReader())
f.read(1)
del f
