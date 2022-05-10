import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(2.5)
    y = ctypes.c_double()

s = S()
print(s.y)
</code>
Python 3.5
<code>from ctypes import *

class S(Structure):
    _fields_ = [("x", c_double, 2.5),
                ("y", c_double)]

s = S()
print(s.y)
</code>
But in Python 2.7, <code>ctypes.Structure</code> does not have a <code>_fields_</code> attribute:
<code>&gt;&gt;&gt; hasattr(ctypes.Structure, '_fields_')
False
</code>
That's why in Python 2.7, you have to do this instead:
<code>from ctypes import *

class S(Structure):
    x = c_double(2.5)
    y = c_double()

s = S()
print(s.y)
</code>

