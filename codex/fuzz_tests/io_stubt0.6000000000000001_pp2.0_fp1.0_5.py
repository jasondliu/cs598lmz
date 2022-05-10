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

Here is another approach, using a <code>io.BytesIO</code> object:
<code>import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)

# create a view on the buffer
b = io.BytesIO(view)

# read from the view
b.read(1)

del f, b
</code>

As suggested by @JohnGordon, here is a variation that uses a <code>memoryview</code>:
<code>import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)

# create a view on the buffer
b = memoryview(view)

# read from the view
b[0]


