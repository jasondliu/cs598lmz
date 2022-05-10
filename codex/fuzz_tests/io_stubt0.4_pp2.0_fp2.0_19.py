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
gc.collect()

# check that the buffer was released
if sys.version_info[:2] >= (2, 7):
    assert view[0] == 0

# check that the buffer is still usable
view[0] = ord('x')
print(view)

# check that the buffer is still writable
view[0] = ord('y')
print(view)
