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
Output:
<code>b''
</code>
I have no idea if this is intended or a bug, but I was going to ask on the python bug tracker, until I realized that the BufferedReader.readinto method would have to be reimplemented by all BufferedReader subclasses, so maybe it's intentional.

