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

# Now try to access the buffer.
try:
    view[0]
except NameError:
    print('SKIP')
    raise SystemExit

# This should fail, since the buffer has been released.
try:
    view[0] = 1
except BufferError:
    print('BufferError')
