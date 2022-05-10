import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(ctypes.c_double):
    def __repr__(self):
        return 'D(%r)' % (ctypes.c_double.__repr__(self),)

class S(ctypes.Structure):
    _fields_ = [('d', D)]

s = S()
s.d = D(42)
print repr(s.d)
</code>
Output:
<code>D(42.0)
</code>

