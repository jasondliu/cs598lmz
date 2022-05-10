import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# Note that the code below is only valid for Python 2.7 and 3.2
del S
del ctypes
</code>
I first noticed this in a call to <code>type(ctypes.Structure._fields_[0])</code>, which was returning <code>ctypes.CField</code>.
The structure class is derived from <code>object</code> in Python 3. So I am wondering if I could use <code>CField = type(S())</code> instead of <code>CField = type(S.x)</code>.
Any idea what's going on here?

