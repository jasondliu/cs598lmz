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
gc.collect()

# test that gc doesn't crash on a broken __del__
class X(object):
    def __del__(self):
        self.x

X()
