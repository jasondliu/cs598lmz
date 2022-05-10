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
assert len(view) == 1

class File(io.RawIOBase):
    def readinto(self, buf):
        raise OSError
    def readable(self):
        return True
    def seekable(self):
        return False
    def writable(self):
        return True

f = io.BufferedReader(File())
try:
    f.read(1)
except OSError:
    pass
else:
    assert 0
f.close()

f = io.BufferedWriter(File())
# Writing to a non-seekable stream with an unbuffered layer above
# does not work.  But we can always flush the write buffer
f.write(b'x')
f.flush()
f.close()

# Writing to a non-seekable stream with a buffered layer above
# works in a safe way.
f = io.BufferedWriter(File(), 1)
try:
    f.write(b'x' * 100)
except OSError:
    pass
else:
    assert 0
f
