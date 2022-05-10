import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_short
    z = ctypes.c_char

s = S()
print hex(ctypes.addressof(s.x))
print hex(ctypes.addressof(s.y))
print hex(ctypes.addressof(s.z))
print hex(ctypes.addressof(s))
</code>
output:
<code>0x7f1fd2c2bfb0
0x7f1fd2c2bfb4
0x7f1fd2c2bfb6
0x7f1fd2c2bfb0
</code>
It's clear that the address of the <code>short</code> member comes after the address of the <code>int</code> member. So that's the reason. Normally, <code>short</code> is 2 bytes, but on a 64-bit system, it's 4 bytes to maintain alignment.

