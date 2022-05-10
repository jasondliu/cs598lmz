import io
# Test io.RawIOBase.readinto

try:
    io.RawIOBase.readinto
except AttributeError:
    print("SKIP")
    raise SystemExit

class RIO(io.RawIOBase):
    def readinto(self, b):
        print("readinto", b)
        b[0:2] = b"hi"
        return 2

r = RIO()
b = bytearray(5)
r.readinto(b)
print(b)
