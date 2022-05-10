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
print(view)

# Simple test of writable() inherited from RawIOBase
f = io.BufferedWriter(File())
print(f.writable())
f.close()
print(f.writable())

# Test of miscellaneous methods
import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
        return 1

f = io.BufferedReader(File())
print(f.read(4))
print(f.tell())
f.seek(0)
print(f.tell())
print(f.read(4))
print(f.peek(4))
print(f.read(4))
print(f.read(4))
print(f.read(4))
print(f.read(4))
f.seek(0)
print(f.read(4))
print(f.read(4))
print(f.getvalue())
print(view)
print(f.getbuffer())
del f
print(view)

# Test of detach()

