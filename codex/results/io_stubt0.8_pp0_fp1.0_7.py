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

sys.stdout.buffer.write(b'X')

f = io.BufferedReader(File())
f.read(2)
del f

sys.stdout.buffer.write(b'Y')

f = io.BufferedReader(File())
f.read(3)
del f

sys.stdout.buffer.write(b'Z')

del view
gc.collect()

sys.stdout.buffer.write(b'\n')


# check that the buffer memory view is properly refcounted
class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
buf = f.read(1)
del buf

sys.stdout.buffer.write(b'X')

f = io.BufferedReader(File())
buf = f.read(2)
del buf

sys.stdout.buffer.write(b'Y')

f = io.BufferedReader
