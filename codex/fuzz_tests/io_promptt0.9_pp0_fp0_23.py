import io
# Test io.RawIOBase
b = bytearray(10)
r = io.RawIOBase()
print("RawIOBase buffer equals None:", r.readinto(b) == None)
