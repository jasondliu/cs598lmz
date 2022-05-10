import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f, view
</code>
Output:
<code>&gt;&gt;&gt; view
c_ubyte(0)
</code>

