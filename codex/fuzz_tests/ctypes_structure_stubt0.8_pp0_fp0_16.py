import ctypes

class S(ctypes.Structure):
    x = ctypes.POINTER(ctypes.c_int)

s = S((ctypes.c_int * 4)(1, 2, 3, 4))
s.x.contents.value
</code>
Result
<code>1
</code>

Using a ctypes <code>Array</code>
<code>import ctypes

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int * 4)]

s = S((1, 2, 3, 4))
s.x[0]
</code>
Result
<code>1
</code>

