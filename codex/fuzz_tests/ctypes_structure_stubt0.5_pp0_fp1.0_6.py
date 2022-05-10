import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float
    y = ctypes.c_float
    z = ctypes.c_float
    w = ctypes.c_float

a = S()
a.x = 1
a.y = 2
a.z = 3
a.w = 4

b = S()
b.x = 5
b.y = 6
b.z = 7
b.w = 8

print(a.x, a.y, a.z, a.w)
print(b.x, b.y, b.z, b.w)

c = a.x + b.x

print(c)
</code>
This works fine, but in this case I have to manually write <code>a.x + b.x</code>, <code>a.y + b.y</code>, <code>a.z + b.z</code>, <code>a.w + b.w</code>.
Is there any way to do this automatically? Something like <code>c = a + b</code>?


A:

You can overload
