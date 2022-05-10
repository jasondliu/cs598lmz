import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p

class U(ctypes.Union):
    _fields_ = [("x", ctypes.c_void_p),
                ("y", ctypes.c_void_p)]

for T in S, U:
    t = T()
    t.x = 1
    print t.y
</code>
which gives
<code>&lt;__main__.LP_c_void_p object at 0x00E9F7B0&gt;
1
</code>
which is exactly what I want.  But how do I fix the code so that I can do
<code>t.y = 2
print t.x
</code>
and have it print <code>2</code>?


A:

<code>t.x</code> and <code>t.y</code> are not the same.  <code>t.x</code> is the <code>ctypes.c_void_p</code> instance which is the field, whereas <code>t.y</code> is a property which returns the value
