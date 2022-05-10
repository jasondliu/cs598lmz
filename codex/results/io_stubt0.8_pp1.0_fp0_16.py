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
uncollectable = [view]

for i in xrange(iterations):
    view[0] = chr(i)
    del view
    view = None
    uncollectable.append(view)

del uncollectable[:]
