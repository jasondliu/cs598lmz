import ctypes

class S(ctypes.Structure):
    x = 42
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", ctypes.c_int),
        ("d", ctypes.c_int),
    ]


p = ctypes.create_string_buffer(ctypes.sizeof(S))

s = ctypes.cast(ctypes.pointer(p), ctypes.POINTER(S)).contents

s.a = 1
s.b = 2
s.c = 3
s.d = 4

print(s)

b = bytes(p)
print(b)

print(ctypes.from_buffer_copy(p, S).a)
</code>
This prints
<code>&lt;__main__.S object at 0x7f3d5905d8e0&gt;
b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x
