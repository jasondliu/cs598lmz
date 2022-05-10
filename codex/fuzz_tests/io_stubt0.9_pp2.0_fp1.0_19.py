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
nj_undefined(view)

nj_unequal(len(b''), 0)

# TODO:
# - nj_undefined_or_empty(0, 1, 2, 3, None)
# - nj_unequal(b'one', 2, 3, 4, 5, 6)
