import io
# Test io.RawIOBase
print("io.RawIOBase")
f = io.BytesIO()
print("io.RawIOBase.read() = %s" % f.read())
print("io.RawIOBase.readinto() = %s" % f.readinto(bytearray(1)))
