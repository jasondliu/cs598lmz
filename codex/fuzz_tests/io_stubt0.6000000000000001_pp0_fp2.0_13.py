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
Now <code>view</code> is a bytearray with a view onto the buffer of <code>f</code>'s buffer. It's no longer valid to access the buffer of <code>f</code>, so this is also a good example of why you don't want to do this.

