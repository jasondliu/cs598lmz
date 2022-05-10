import ctypes

class S(ctypes.Structure):
    x = ctypes.c_bool
    y = ctypes.c_bool
    z = ctypes.c_bool

s = S(False, False, False)
print(s.x, s.y, s.z)
</code>
This correctly prints <code>False False False</code> but I would like to have some way of initializing it as <code>S(True, True, True)</code> instead.  Is there an automatic way to do this?  I know I could just write <code>S(True, True, True)</code> but I would like to avoid this because I have a lot of fields, and it's not always clear what the default value is.


A:

You could use a class factory:
<code>def S(**kwargs):
    class S(ctypes.Structure):
        x = ctypes.c_bool
        y = ctypes.c_bool
        z = ctypes.c_bool
    s = S()
    for k, v in kwargs.items():
        setattr(s, k, v)
    return s

