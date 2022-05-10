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
Instead, if you don't care about the situation when multiple different objects with the same data representation exist at the same time, you can use <code>bytes</code>:
<code>import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = memoryview(buf)
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
</code>

