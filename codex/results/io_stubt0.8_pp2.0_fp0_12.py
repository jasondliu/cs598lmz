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

# Check it's a zero-terminated string
print(view[:10])
print(view[0] == 0)
</code>

