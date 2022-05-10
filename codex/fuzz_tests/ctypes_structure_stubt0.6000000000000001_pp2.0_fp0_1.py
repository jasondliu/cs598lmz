import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

p = ctypes.pointer(S(1, 2))

print p.contents.x
print p.contents.y
</code>
The <code>pointer</code> class has a <code>contents</code> attribute that gives you access to the fields of the struct. The <code>contents</code> attribute is read-write, so you can also set the fields like this:
<code>p.contents.x = 42
</code>

