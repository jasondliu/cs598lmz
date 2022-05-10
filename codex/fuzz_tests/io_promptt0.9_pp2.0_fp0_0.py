import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def __init__(self, a, b=None):
        self.a = a
        self.b = b

    def readinto(self, b):
        b[0:2] = (520, 1314)
        return 2

    def write(self, b):
        print(self.a, self.b, b)

try:
    with MyRawIO(10, 31) as f:
        print(f.a, f.b)
except AttributeError:
    print("SKIP")
    raise SystemExit

buf = bytearray(6)
f = MyRawIO(10, 31)
f.readinto(buf)
print(buf[0:2])
f.write(b'hello')
f.write(b' world!')

# Test io.BytesIO
with io.BytesIO() as f:
    f.write(b"hello world")
    f.seek(0)
    f.truncate()

a = 50
b = 10000
f
