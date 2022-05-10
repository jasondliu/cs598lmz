import io
# Test io.RawIOBase.readinto()

# Bytearray as destination should work
b = bytearray(3)
io.BytesIO(b"abc").readinto(b)
assert b == b"abc"

# Mutable buffer should work
