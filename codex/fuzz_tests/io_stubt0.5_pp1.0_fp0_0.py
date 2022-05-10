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

def g():
    yield view

it = g()
next(it)
del it

gc.collect()

# If the buffer is not freed, the next line will segfault
gc.collect()
