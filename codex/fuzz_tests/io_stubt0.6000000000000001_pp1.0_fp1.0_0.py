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
sys.getrefcount(view)
</code>

<code>import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = bytearray(buf)
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
sys.getrefcount(view)
</code>

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
sys.getrefcount(view)
</code>

<code>import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = memoryview(buf).cast('B')
    def readable(self):
        return True

f = io.BufferedReader(
