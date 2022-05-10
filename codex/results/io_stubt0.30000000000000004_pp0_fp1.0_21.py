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

del view

# Issue #14094: a BufferedReader should not be able to read from a closed
# RawIOBase.
class MyRawIO(io.RawIOBase):
    def readinto(self, buf):
        return len(buf)
    def readable(self):
        return True
    def close(self):
        pass

f = io.BufferedReader(MyRawIO())
f.close()
try:
    f.read(1)
except ValueError:
    pass
else:
    raise Exception("expected ValueError")

# Issue #14094: a BufferedReader should not be able to read from a closed
# RawIOBase.
class MyRawIO(io.RawIOBase):
    def readinto(self, buf):
        return len(buf)
    def readable(self):
        return True
    def close(self):
        pass

f = io.BufferedReader(MyRawIO())
f.close()
try:
    f.read(1)
except ValueError:
    pass
else:
    raise Exception
