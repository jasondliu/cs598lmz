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
<code>b''
</code>
The buffer is cleared since it is <code>del</code>ed when the <code>BufferedReader</code> is closed. Python would be clearing <code>view</code> anyway, but the <code>BufferedReader</code> closes early so it can clear the buffer.
If the <code>BufferedReader</code> is closed early, the <code>File</code> object will still be alive.
<code>import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
print(view)
</code>
<code>b''
</code>
This will print <code>b''</code>, since <code>view</code> has been cleared when <code>f</code> was closed.

