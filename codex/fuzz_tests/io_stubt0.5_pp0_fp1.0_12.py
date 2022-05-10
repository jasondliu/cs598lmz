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
If you want to use <code>io.open</code> instead, you can use a <code>io.BytesIO</code> object:
<code>import io

f = io.BytesIO(b'a')
buf = f.read(1)
del f
print(buf)
</code>

