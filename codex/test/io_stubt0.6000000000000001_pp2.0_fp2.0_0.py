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

f = io.BufferedReader(File())
del f
print(view)

# Test the error handling in readinto
f = io.BufferedReader(io.BytesIO(b"foo"))
def readinto(buf):
    raise ValueError()
f.raw.readinto = readinto
try:
    f.readinto(bytearray(1))
except ValueError:
    pass
else:
    print("ValueError should have been raised")

f = io.BufferedReader(io.BytesIO(b"foo"))
def readinto(buf):
    buf[0] = ord("a")
    return 0
f.raw.readinto = readinto
print(f.readinto(bytearray(1)))

# Issue #3650: return type of BufferedReader.readinto()
class EmptyFile(io.RawIOBase):
    def readinto(self, buf):
        return 0
    def readable(self):
        return True
f = io.BufferedReader(EmptyFile())
