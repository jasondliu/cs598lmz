import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.resize(S, 0)

def callback(p):
    print p, S.x

ctypes.resize(S, ctypes.sizeof(ctypes.CField) + ctypes.sizeof(S.x))
S.x = ctypes.pointer(S.x)

ctypes.resize(S, 0)
S.x = ctypes.cast(S.x, ctypes.CFUNCTYPE(ctypes.c_int, S))

s = S()
s.x(s)
</code>
When I was writing this code, I was thinking that I could have done something like
<code>ctypes.resize(S, ctypes.sizeof(ctypes.CField) + ctypes.sizeof(S.x))
S.x = ctypes.cast(S.x, ctypes.CFUNCTYPE(ctypes.c_int, S * 0))
</code>
since everything that is known about the <code>S</code> structure at this point was its length (which is 0).  However,
