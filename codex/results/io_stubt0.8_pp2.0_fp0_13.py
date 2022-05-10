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
del File
import io

buf = bytearray(1)
def readinto(buf):
    global view
    view = buf
f = io.BufferedReader(readinto)
f.read(1)
del f
del readinto
import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def fileno(self):
        return 0
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
del File
import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        raise ValueError

f = io.BufferedReader(File())
try:
    f.read(1)
except ValueError:
    pass
else:
    raise ValueError
del f
del File
import io
import _io

class File(io.RawIOBase):
    def readinto(self
