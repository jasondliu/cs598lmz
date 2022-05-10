import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint64
    y = ctypes.c_int64

s = S()
s.x = 0x7fffffffffffffff
print s.x
print s.y

s.y = 0x8000000000000000
print s.x
print s.y

s.x = 0xffffffffffffffff
print s.x
print s.y

s.y = 0xffffffffffffffff
print s.x
print s.y

s.x = 0x7fffffffffffffff
print s.x
print s.y
</code>
results in
<code>9223372036854775807
0
9223372036854775807
-9223372036854775808
9223372036854775807
-1
9223372036854775807
-1
9223372036854775807
-9223372036854775808
</code>

