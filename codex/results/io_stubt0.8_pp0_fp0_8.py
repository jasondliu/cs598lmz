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
f.flush()
f.write(b"def")
f.flush()
f.raw.close()

f = io.BufferedWriter(File(), 100)
f.write(b"x"*100)
f.write(b"y"*100)
f.write(b"z"*100)
f.flush()

f.raw.close()

f = io.BufferedWriter(File(), 100)
f.write(b"x"*100)
f.write(b"y"*100)
f.write(b"z"*100)
f.close()

try:
    f.write(b"foo")
except ValueError:
    print("ValueError")

f.raw.close()

try:
   
