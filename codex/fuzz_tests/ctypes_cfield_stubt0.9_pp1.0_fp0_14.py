import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
print(type(S.x))
print(S.x.type)
print(S.x.ofs)

s = S()
v = ctypes.c_int(10)
ctypes.set_c_type(s, 'x', v)
print(s.x)
print(type(s.x))

ctypes.temporary_field(s, 'x', ctypes.c_int(20))
print(s.x)
print(type(s.x))
