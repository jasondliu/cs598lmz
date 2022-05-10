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

# issue 1: buf is alive longer than view
print(view)

# issue 2: dummy refs to buf are alive longer than view
buf, dummy = None, None
print(view)

# issue 3: one view is overwritten by another
del view
x = b'x'
f = io.BufferedReader(File())
