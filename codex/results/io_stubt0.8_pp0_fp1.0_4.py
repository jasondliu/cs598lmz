import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f, File

print bytearray(view[:10])

a = long(0)
a += 1
print a
b = "abc"
a = long(b[0]) + a
print a
c = 10.1
a = float(b[0]) + a
print a

import sys
stream = sys.stdout
print stream.write("Hello World!")
