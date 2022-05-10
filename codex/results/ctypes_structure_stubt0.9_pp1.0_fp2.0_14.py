import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
</code>
The above code will do it.  I have changed it to:
<code>S.x.__doc__ = "hello"
S.y.__doc__ = "world"
</code>
And it started working.

