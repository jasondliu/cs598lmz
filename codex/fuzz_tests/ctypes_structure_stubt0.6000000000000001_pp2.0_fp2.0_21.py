import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float(1.0)
    _fields_ = [('x', ctypes.c_float)]

s = S()
print s.x
s.x = 2.0
print s.x
</code>

<code>1.0
2.0
</code>


A:

<code>class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_float)]
s = S()
print s.x
s.x = 2.0
print s.x
</code>
will print
<code>0.0
2.0
</code>
I think this is expected.

