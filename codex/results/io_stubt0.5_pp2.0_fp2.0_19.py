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
I've tried to use a <code>io.BufferedReader</code> to read 1 byte from the file, but the <code>view</code> is never touched. I am wondering if there is a way to do this in Python?

