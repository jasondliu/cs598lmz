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
</code>
Running this on Python 3.6.5 on Mac OS X, I get:
<code>b'\x00'
</code>
...which indicates that the <code>readinto</code> method did not get a slice of <code>buf</code> but got the whole <code>bytearray</code> object.  This isn't a problem with the <code>f</code> that's created on my machine because the <code>readinto</code> method can't write more than a single byte, but it's a potential problem if the <code>readinto</code> method could write more than a single byte to the buffer.

