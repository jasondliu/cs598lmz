import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte
    y = ctypes.c_ubyte

a = ctypes.c_ubyte(1)
b = ctypes.c_ubyte(2)
c = ctypes.c_ubyte(3)
d = ctypes.c_ubyte(4)

s = S(*[a, b])

print s.x, s.y

s.x = c
s.y = d

print s.x, s.y

print a, b, c, d

print s._fields_

s2 = S(*[a, b])

print s2.x, s2.y

s2.x = c
s2.y = d

print s2.x, s2.y

print a, b, c, d

print s2._fields_

print s._fields_
</code>
Output:
<code>1 2
3 4
1 2 3 4
[('x', c_ubyte), ('y', c_ubyte)]
