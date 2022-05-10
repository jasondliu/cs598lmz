import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.CField)]
TypeError: expected a type object
</code>
I know I can do this:
<code>class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int, 1)]
</code>
But that's not what I want.  I want the <code>ctypes.CField</code> type to be recognized.

