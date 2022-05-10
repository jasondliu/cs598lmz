import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n):
        return self.f.read(n)
    def write(self, b):
        return self.f.write(b)
    def close(self):
        self.f.close()

f = open("/tmp/x", "w")
f = File(f)

f.write(b"abc")
f.close()

f = open("/tmp/x", "r")
print(f.read())
f.close()

# -------------------------------------------------

class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n):
        return self.f.read(n)
    def write(self, b):
        return self.f.write(b)
    def close(self):
        self.f.close()

f = open("/tmp/x", "w")
f = File(f)

f.write(b"abc")
