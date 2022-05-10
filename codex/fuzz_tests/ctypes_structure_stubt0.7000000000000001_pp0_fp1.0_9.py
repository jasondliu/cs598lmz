import ctypes

class S(ctypes.Structure):
    x = None

    _fields_ = [('x', ctypes.c_int)]

s = S()
print(s.x)
</code>
In the above example, <code>s.x</code> is set to <code>None</code>, but the <code>_fields_</code> declaration is ignored.
The reason you need <code>_fields_</code> is because <code>ctypes</code> doesn't have any meta classes, so <code>ctypes</code> can't detect that you've created a new attribute to the class and automatically make that part of the structure.

