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
import gc
gc.collect()
view
1 in view

class File(io.RawIOBase):
    def write(self, buf):
        pass
    def writable(self):
        return True

f = io.BufferedWriter(File())
f.write(b"abc")
