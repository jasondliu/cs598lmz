import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ]

s = S(3, 4)
s.x = 1
s.y = 2
s.z = 3
s.w = 4
s.a = 5
print(s.x, s.y, s.z, s.w, s.a)
</code>
Output:
<code>1 2 3 4 5
</code>
That's because <code>ctypes.Structure</code> is a subclass of <code>ctypes._SimpleCData</code>, which is a subclass of <code>object</code>:
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; help(ctypes.Structure)
class Structure(ctypes._SimpleCData)
 |  Structure(self, *args, **kw)
 |  
 |  Create a new Structure subclass, and call it.
 |  
 |
