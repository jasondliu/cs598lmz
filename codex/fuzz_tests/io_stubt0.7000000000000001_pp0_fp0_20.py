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
</code>
If I run the above example in Python 3.6, <code>view</code> will contain a bytearray of length 1 (with the first byte set to 0). If I run the above example in Python 3.7, <code>view</code> will contain a bytearray of length 0.
To me, that looks like a bug in Python 3.7. It doesn't seem to be documented anywhere, though. Is this really a bug? If so, how can I report it?

