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
This is just a proof of concept, but I think it is a good idea to use a <code>io.BufferedReader</code> to read your data, because it will handle the buffering for you.

