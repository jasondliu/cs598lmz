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
But it's not working, the <code>del f</code> line gives the error <code>ReferenceError: weakly-referenced object no longer exists</code>. What's wrong?


A:

You need to implement your own <code>close()</code> method to avoid the default implementation's <code>del self.raw</code> statement.
<code>class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True
    def close(self):
        return

f = io.BufferedReader(File())
f.read(1)
del f
</code>

