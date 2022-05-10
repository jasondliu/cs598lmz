import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    a = ctypes.c_int
    b = ctypes.c_int
    c = ctypes.c_int
    d = ctypes.c_int
    e = ctypes.c_int
    f = ctypes.c_int
    g = ctypes.c_int
    h = ctypes.c_int
    i = ctypes.c_int

s = S()
s.x = 1
print s.x
print s.y
print s.z
x = s.x
y = s.y
z = s.z
print x
print y
print z
</code>
I was surprised that <code>s.y</code> and <code>s.z</code> were 0.
Is this expected behaviour?  I'm confused as I've thought that structures would automatically set members to <code>0</code>, like arrays.


A:

It's the same as in C.  If you don't initialize explicitly, members
