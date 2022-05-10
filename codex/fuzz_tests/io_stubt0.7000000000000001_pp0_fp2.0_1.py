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

While a bug, this is an excellent example of why you want to be careful with the object model and make sure you know what you're doing if you're going to subclass the core types.

