import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longdouble(123.0)
    y = ctypes.c_longdouble(234.0)

s = S()
p = ctypes.pointer(s)

print s.x
print p.contents.x
</code>
Here <code>s</code> is a <code>ctypes.Structure</code> instance, and <code>p</code> is a <code>ctypes.POINTER(S)</code> instance. The <code>contents</code> attribute of the <code>POINTER</code> instance gives you a reference to the <code>Structure</code> instance.

