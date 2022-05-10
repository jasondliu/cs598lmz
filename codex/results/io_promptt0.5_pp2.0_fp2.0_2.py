import io
# Test io.RawIOBase.readinto()
try:
    io.RawIOBase.readinto
except AttributeError:
    import sys
    print("SKIP")
    sys.exit()

class MyRawIO(io.RawIOBase):
    def readinto(self, buf):
        print("readinto")
        buf[0] = ord('a')
        return 1

m = MyRawIO()
buf = bytearray(5)
print(m.readinto(buf))
print(buf)
