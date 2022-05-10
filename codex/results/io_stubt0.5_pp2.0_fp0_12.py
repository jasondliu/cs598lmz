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

def f():
    global view
    view[0] = 42
f()
print view
</code>
The output is <code>[42]</code> as expected.

