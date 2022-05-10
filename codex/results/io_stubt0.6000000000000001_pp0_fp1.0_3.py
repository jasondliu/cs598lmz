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
sys.stdout.buffer.write(view)

class File(io.RawIOBase):
    def readinto(self, buf):
        buf[:] = b'x'
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
sys.stdout.buffer.write(view)

class File(io.RawIOBase):
    def readinto(self, buf):
        buf[:] = b'x' * len(buf)
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
sys.stdout.buffer.write(view)

class File(io.RawIOBase):
    def readinto(self, buf):
        buf[:] = b'x' * (len(buf) + 1)
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
sys.stdout.buffer.write(view)

