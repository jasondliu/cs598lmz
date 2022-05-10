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

# Issue #22796: a BufferedReader with a RawIOBase source should
# be able to read() after readinto()
f = io.BufferedReader(File())
f.readinto(bytearray(1))
f.read(1)
del f

# Issue #22796: a BufferedReader with a RawIOBase source should
# be able to readinto() after read()
f = io.BufferedReader(File())
f.read(1)
f.readinto(bytearray(1))
del f

# Issue #22796: a BufferedReader with a RawIOBase source should
# be able to readinto() after readinto()
f = io.BufferedReader(File())
f.readinto(bytearray(1))
f.readinto(bytearray(1))
del f

# Issue #22796: a BufferedReader with a RawIOBase source should
# be able to readinto() after read()
f = io.BufferedReader(File())
f.read(1)
f.readinto(byt
