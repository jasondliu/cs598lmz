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

# Issue #23014: test that the weakref callback is called with the
# correct arguments.

import weakref

class MyFileIO(io.FileIO):
    def close(self):
        self.close_called = True
        io.FileIO.close(self)

f = MyFileIO(__file__, 'r')
r = weakref.ref(f, lambda x, y: y.append((x, f)))
del f
