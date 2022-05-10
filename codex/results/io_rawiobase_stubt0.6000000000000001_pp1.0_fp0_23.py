import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def readable(self):
        return True
    def readinto(self, b):
        n = len(b)
        b[:n] = self.f.read(n)
        return n
f = open("/etc/passwd", "rb")
b = bytearray(5)
f = File(f)
print(f.readinto(b))
print(b)
print(f.readinto(b))
print(b)

# io.StringIO
import io
f = io.StringIO("initial value")
print(f.read())

# io.BytesIO
import io
f = io.BytesIO(b"initial value")
print(f.read())

# io.TextIOWrapper
import io
s = "你好，世界"
f = io.StringIO(s)
print(f.read())
b = io.BytesIO(s.encode("utf-8"))
print(io.TextI
