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
This last example is a bit of a hack, but I believe it is the only way to do it. If you're looking for a more readable solution, you can make a subclass of <code>io.BufferedReader</code> to do this.

