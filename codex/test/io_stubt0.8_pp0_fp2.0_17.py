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

# Test that the weakref callback is not called until the gc collects the
# garbage.
alive = []
def callback(wr, alive=alive):
    alive.append(wr())
