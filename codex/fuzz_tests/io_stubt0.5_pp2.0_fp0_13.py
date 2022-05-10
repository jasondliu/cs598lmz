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
This prints out the first byte of the <code>buf</code> passed to <code>readinto</code> (which is the first byte of the <code>view</code> object).
If you really want to get tricky, you can make <code>File</code> a <code>io.RawIOBase</code> subclass, and use <code>io.open</code> to open it:
<code>import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

with io.open(File()) as f:
    f.read(1)

print(view)
</code>

