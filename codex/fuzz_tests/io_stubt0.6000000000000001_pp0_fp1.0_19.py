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

# io.TextIOBase

class File(io.TextIOBase):
    def read(self, size=-1):
        return "abc"
    def readable(self):
        return True

f = io.TextIOWrapper(File())

print(f.read(1))
print(f.read())
print(f.read())

# io.BufferedReader

class RawBytesIO(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

class TextIO(io.TextIOBase):
    def read(self, size=-1):
        return "abc"
    def readable(self):
        return True

r = io.BufferedReader(RawBytesIO())
t = io.BufferedReader(TextIO())

print(r.read(1))
print(r.read())
print(r.read())

print(t.read(1))
print(t.read())
print(t.read
