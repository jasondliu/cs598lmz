import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte
    y = ctypes.c_ubyte

s = S()
s.x = 0xA5
s.y = 0x5A
print hex(ctypes.addressof(s))
print hex(ctypes.addressof(s.x))
print hex(ctypes.addressof(s.y))
</code>
Prints
<code>0x7ffd8f9e9ff0
0x7ffd8f9e9ff0
0x7ffd8f9e9ff1
</code>
So it seems like the address of the structure is the same as the address of the first member.

