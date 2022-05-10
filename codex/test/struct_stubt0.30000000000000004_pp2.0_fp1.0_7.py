from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()

# Create a buffer
import io
b = io.BytesIO()

# Write a record
values = (1, b'ab', 2.7)
print('Original:', values)
print()

print('ctypes string buffer')
import ctypes
b = ctypes.create_string_buffer(s.size)
print(b)

# Write to the buffer
print('Before  :', s.unpack_from(b))
s.pack_into(b, 0, *values)
print('After   :', s.unpack_from(b))
print()

print('array')
import array
a = array.array('b', b'\0' * s.size)
print(a)

# Write to the buffer
print('Before  :', s.unpack_from(a))
s.pack_into(a, 0, *values)
print('After   :', s.unpack_from(a))
print()

