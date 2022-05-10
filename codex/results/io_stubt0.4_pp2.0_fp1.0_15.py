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

view[0] = 0

# XXX: This test is not very good. It should test that the view is
# cleared, not just that the buffer is cleared.
print(view[0])
