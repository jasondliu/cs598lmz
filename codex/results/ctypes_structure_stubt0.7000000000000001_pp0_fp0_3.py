import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32
    y = ctypes.c_int32

class B(ctypes.Structure):
    _fields_ = [('b', ctypes.c_char),
                ('s', S)]

b = B()
b.b = b'b'
b.s.x = 0x12345678
b.s.y = 0x87654321

print(b.b)
print(b.s.x)
print(b.s.y)

#b = bytes(b)
b = bytes(b.b)
print(b)

#p = ctypes.pointer(b)
p = ctypes.pointer(b.b)
print(p.contents)
</code>
output:
<code>b'b'
305419896
-1910541445
b'b'
Traceback (most recent call last):
  File "example.py", line 26, in &lt;module&gt;
    print(p.contents)
  File "C:\Program Files\Python35
