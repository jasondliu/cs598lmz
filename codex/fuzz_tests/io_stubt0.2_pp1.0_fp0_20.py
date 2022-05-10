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

# This is a test of the "del" statement.

# del x
# del x, y
# del x.y
# del x.y, z
# del x.y.z
# del x.y.z, a
# del x[y]
# del x[y], z
# del x[y][z]
# del x[y][z], a
# del x[y:z]
# del x[y:z], a
# del x.y[z]
# del x.y[z], a
# del x.y[z:a]
# del x.y[z:a], b
# del x.y.z[a]
# del x.y.z[a], b
# del x.y.z[a:b]
# del x.y.z[a:b], c

# del x, y[z]
# del x, y[z], a
# del x, y[z:a]
# del x, y[z:a], b
# del x, y.z
#
