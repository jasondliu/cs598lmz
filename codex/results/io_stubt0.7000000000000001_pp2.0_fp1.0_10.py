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
view  # [1, 2]
</code>
I think this is because the reference count of <code>view</code> is only 1.
But in the following code, the <code>del</code> statement does not help.
<code>import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
del view
view  # NameError: name 'view' is not defined
</code>
Why?

