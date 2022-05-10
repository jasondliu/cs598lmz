import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float
    y = ctypes.c_float
    z = ctypes.c_float

buffer = ctypes.create_string_buffer(12)

s = S()
s.x = 5
s.y = 12

ctypes.memmove(buffer, ctypes.byref(s), 12)

print(buffer.raw)
</code>


A:

The answer is (for python 3.x):
<code>buffer = ctypes.create_string_buffer(12)
s = S()
s.x = 5
s.y = 12

ctypes.memmove(buffer, ctypes.byref(s), 12)

bytearray(buffer)[:12]
</code>

