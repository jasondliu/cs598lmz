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

print(view.tobytes())
</code>
In this example, the <code>view</code> object will be kept alive at least until the <code>del</code> statement. 

