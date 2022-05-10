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
print(view)

# io.BufferedReader is a wrapper around the raw stream, which
# makes it a bit harder to reproduce the crash.

# It's easy to reproduce the crash with io.BufferedRWPair,
# though.

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True
    def write(self, data):
        pass
    def writable(self):
        return True

f = io.BufferedRWPair(File(), File())
f.read(1)
del f
print(view)
