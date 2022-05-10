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
Here, the <code>view</code> object is still alive, and so is the <code>File</code> object. However, the <code>view</code> object is no longer bound to the <code>File</code> object, and so, if you change the <code>File</code> object, the <code>view</code> object won't be affected.

