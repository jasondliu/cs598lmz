import ctypes
ctypes.cast(offset, ctypes.py_object).value = (1, 2)
print(offset[0])
print(offset[1])

# Create an array of 8-byte doubles
import array
a = array.array('d', range(0,8))
print(a)
a.frombytes(b'\x00\x01\x02\x03\x04\x05\x06\x07')
print(a)

# Change the byte order
a.byteswap()
print(a)

# Get the byte order
print(a.typecode)
print(a.itemsize)

# Convert to a list
print(a.tolist())

# Create a memoryview
m = memoryview(a)
print(m)

# Create a memoryview with read-only access
m2 = memoryview(a).cast('B')
print(m2)

# Convert to a bytearray and read the first byte
print(m2.tobytes()[0])

# Assign the first byte of the original array
a[0
