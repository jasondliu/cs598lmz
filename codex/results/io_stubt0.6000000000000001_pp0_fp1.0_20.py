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

# io.BufferedReader does not allow reading after closing.
try:
    f.read(1)
except ValueError:
    pass
else:
    raise Exception("expected an exception")

# But it does not matter if the underlying file is closed.
view[0] = 0xff

# The underlying file must not be closed when the view is used.
