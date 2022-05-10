import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(5)
    y = ctypes.c_int(6)

s = S()
print(s.x, s.y)
print(s.x.value, s.y.value)

s.x = ctypes.c_int(7)
s.y = ctypes.c_int(8)
print(s.x, s.y)
print(s.x.value, s.y.value)

s = ctypes.create_string_buffer(b"hello")
print(s.raw) # b'hello'
print(s.value) # b'hello'

s.value = b"world"
print(s.raw) # b'world'
print(s.value) # b'world'

print(ctypes.sizeof(ctypes.c_wchar(1)))
print(ctypes.sizeof(ctypes.c_char(1)))
print(ctypes.sizeof(ctypes.c_byte(1)))
print(ctypes.sizeof(ctypes.c_short
