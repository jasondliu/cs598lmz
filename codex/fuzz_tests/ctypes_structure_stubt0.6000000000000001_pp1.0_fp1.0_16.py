import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

print(S.x.offset)
print(S.x.size)
print(ctypes.sizeof(S))

s = S()
print(ctypes.addressof(s))
print(ctypes.addressof(s.x))

s2 = ctypes.cast(ctypes.addressof(s), ctypes.POINTER(S))
print(s2.contents.x)

s3 = S()
s3.x = 42
print(s3.x)
print(s2.contents.x)
</code>
prints
<code>0
4
4
140682970429728
140682970429728
0
42
42
</code>

