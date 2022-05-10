import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)  # i prefer 'CField'
</code>
Then I can just compare the variable with <code>CField</code> if I'm looking for c types.

