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

# test that the buffer is cleared when the file is deleted
assert view == 0

# test that a new buffer is allocated when the file is read again
f = io.BufferedReader(File())
f.read(1)
assert view != 0

# test that the buffer is cleared when the file is closed
f.close()
assert view == 0

# test that a new buffer is allocated when the file is read again
f = io.BufferedReader(File())
f.read(1)
assert view != 0

# test that the buffer is cleared when the file is deleted
del f
assert view == 0

# test that a new buffer is allocated when the file is read again
f = io.BufferedReader(File())
f.read(1)
assert view != 0

f.close()

# test that a new buffer is allocated when the file is read again
f = io.BufferedReader(File())
f.read(1)
assert view != 0

# test that the buffer is cleared when the file is closed
f.detach()
assert view == 0

#
