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

# check that the view is still alive
view[0] = ord('x')

# check that we can create a new view
view = memoryview(b'abcdefghijklmnopqrstuvwxyz')
view[0] = ord('x')

# check that the old view is dead
try:
    view[0] = ord('x')
except ValueError:
    pass
else:
    raise Exception

# check that we can create a new view again
view = memoryview(b'abcdefghijklmnopqrstuvwxyz')
view[0] = ord('x')
