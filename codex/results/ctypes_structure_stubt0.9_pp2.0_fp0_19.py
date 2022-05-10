import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int.fwdprop
    y = ctypes.c_int.fwdprop
    z = ctypes.c_int.fwdprop

s = S()
S.x.fget(s)
S.x.fset(s, 2)
print(S.x.fget(s))

S.y.fget(s)
S.y.fset(s, 11)
print(S.y.fget(s))

S.z.fget(s)
S.z.fset(s, 92)
print(S.z.fget(s))
