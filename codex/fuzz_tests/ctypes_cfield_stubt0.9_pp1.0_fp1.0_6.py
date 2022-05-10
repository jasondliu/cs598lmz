import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

s = S()
s.x = -1234
s.x = -1
</code>
And there you are, <code>s.x</code> is now really, really big.

