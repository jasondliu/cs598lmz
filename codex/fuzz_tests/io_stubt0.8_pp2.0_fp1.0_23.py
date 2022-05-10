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
# find the Pinned object
pinned = view[-16]
print pinned
print hex(id(pinned))

def f(pinned):
    print hex(id(pinned))

f(pinned)

# returns 4391160
# returns 6232864
