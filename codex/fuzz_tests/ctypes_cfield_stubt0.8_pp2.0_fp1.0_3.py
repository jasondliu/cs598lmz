import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

s = S()
s.x = 100

print(s.x)
print(S.x)
print(S.x.type)
print(S.x.offset)
print(S.x.size)
print(S.x.name)
print(S.x.from_address)
print(S.x.from_address.__self__)
