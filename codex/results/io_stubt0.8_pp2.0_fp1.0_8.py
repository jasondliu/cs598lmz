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
# f is now closed

# Now, we can get buf directly
assert view == b'\0'
</code>
This is a bit of a hack.  If you need to be sure of the internal buffer held by the stream, you may have to look at the C code in <code>_io</code>.

