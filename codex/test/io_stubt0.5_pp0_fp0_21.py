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

# This is the same as sys.stdout, except that it's a BufferedReader.
# When sys.stdout.write() is called, it calls the write method of its
# underlying buffer, which is this BufferedReader. The BufferedReader
# then calls its underlying raw stream, which is our File object. The
# File object then calls the readinto() method of the buffer that was
# passed to it, which is view.

# So, when sys.stdout.write() is called, the string is written to the
# view object, which happens to be the same object as the b"abc" string.

# This should cause the b"abc" string to be changed to b"a" (or b"\0"
# if you're running in Python 3).

