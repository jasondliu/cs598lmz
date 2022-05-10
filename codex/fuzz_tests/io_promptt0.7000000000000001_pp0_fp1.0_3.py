import io
# Test io.RawIOBase.readinto()

# Bytearray as destination should work
b = bytearray(3)
io.BytesIO(b"abc").readinto(b)
assert b == b"abc"

# Mutable buffer should work
b = array.array('b', [0, 1, 2])
io.BytesIO(b"abc").readinto(b)
assert b == array.array('b', [97, 98, 99])

# Read-only buffer should work
b = memoryview(bytearray(3))
io.BytesIO(b"abc").readinto(b)
assert b == b"abc"

# Subview of array should work
b = array.array('b', [0, 1, 2, 3, 4, 5])
b = memoryview(b)[2:5]
io.BytesIO(b"abc").readinto(b)
assert b == b"abc"

# Invalid type should fail
b = None
try:
    io.BytesIO(b"abc").readinto(b)
except TypeError:
    pass
else
