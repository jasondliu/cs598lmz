import io
# Test io.RawIOBase.readinto()

# Read into a bytearray
r = io.BytesIO(b"01234567890")
b = bytearray(5)
n = r.readinto(b)
print(n, b)

# Read into a memoryview
r = io.BytesIO(b"01234567890")
b = bytearray(5)
m = memoryview(b)
n = r.readinto(m)
print(n, b)

# Read into a read-only memoryview
r = io.BytesIO(b"01234567890")
b = bytearray(5)
m = memoryview(b).cast('B')
n = r.readinto(m)
print(n, b)

# Read into a read-only buffer
r = io.BytesIO(b"01234567890")
b = bytearray(5)
