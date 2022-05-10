import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(1.0)
    y = ctypes.c_double(1.0)
    _pack_ = 1 #must be set to 1

s = S()
print(s)
s.y = 2.0
print(s)
</code>
The output of this is
<code>(1.0, 1.0)
(1.0, 2.0)
</code>
However if we change the order of <code>x</code> and <code>y</code> in the class definition we get
<code>class S(ctypes.Structure):
    y = ctypes.c_double(1.0)
    x = ctypes.c_double(1.0)
    _pack_ = 1

s = S()
print(s)
s.y = 2.0
print(s)
</code>
The output of which is
<code>(1.0, 0.0)
(1.0, 2.0)
</code>
Why is this? It seems like changing the order of the attributes in a c
