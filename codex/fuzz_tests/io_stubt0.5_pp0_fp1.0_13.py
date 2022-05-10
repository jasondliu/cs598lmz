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

# issue #23603: test that the weakref callback is called even if the
# underlying raw file is not closed
class File2(io.RawIOBase):
    def __init__(self):
        self.closed = False
    def close(self):
        self.closed = True
    def readinto(self, buf):
        return 0
    def readable(self):
        return True

f = io.BufferedReader(File2())
weakref.ref(f, lambda x: f.closed)
del f

# issue #23603: test that the weakref callback is called even if the
# underlying raw file is not closed
class File3(io.RawIOBase):
    def __init__(self):
        self.closed = False
    def close(self):
        self.closed = True
    def readinto(self, buf):
        return 0
    def readable(self):
        return True

f = io.BufferedReader(File3())
weakref.ref(f, lambda x: f.closed)
del f

# issue #23603
