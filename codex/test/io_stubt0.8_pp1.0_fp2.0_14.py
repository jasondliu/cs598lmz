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

# I would have expected this to raise an exception,
# but instead the buffer is still referenced from
# the buffered reader (and released only at the end
# of the testprogram)
view = None
