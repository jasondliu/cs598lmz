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
f = None
f = io.BufferedReader(File())
del f

print(view)
</code>
It prints <code>b''</code>.
The Python interpreter may have freed the data when the <code>io.BufferedReader</code> instance is deleted, but it does not need to. I guess that is the only reason why it is not clearly specified.

